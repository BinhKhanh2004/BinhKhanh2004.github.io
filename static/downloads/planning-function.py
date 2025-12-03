import os
import time
import boto3
import json

# Athena constants
DATABASE = os.environ['glue_db']
TABLE = os.environ['glue_table']

# S3 output for query results
S3_OUTPUT = os.environ['output_bucket']

# SQS queue for sending notifications
QUEUE_URL = os.environ['queue_url']

def lambda_handler(event, context):
    # Athena query: tìm sản phẩm bị thiếu hàng
    query = f"""
        SELECT * FROM {DATABASE}.{TABLE}
        WHERE is_stock_low = true
        AND notification_sent = false;
    """

    client = boto3.client('athena')

    queryStart = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': DATABASE},
        ResultConfiguration={'OutputLocation': S3_OUTPUT}
    )

    queryId = queryStart['QueryExecutionId']
    time.sleep(3)  # chờ query hoàn thành

    alerts = []
    results = client.get_query_results(QueryExecutionId=queryId)

    rowheaders = results['ResultSet']['Rows'][0]['Data']
    rowindex = 0

    for r in results['ResultSet']['Rows']:
        if rowindex == 0:
            rowindex += 1
            continue

        row_dict = {}
        columnindex = 0
        for columnvalue in r['Data']:
            row_dict[rowheaders[columnindex]['VarCharValue']] = columnvalue['VarCharValue']
            columnindex += 1

        store_id = row_dict['store_id']
        product_name = row_dict['product_name']
        alert_msg = f"⚠️ Store {store_id} is low on '{product_name}'. Alerting delivery team."
        alerts.append(alert_msg)

        send_sqs_message(store_id, product_name)

        rowindex += 1

    return alerts

def send_sqs_message(store_id, product_name):
    client = boto3.client('sqs')
    
    message = {
        "store_id": store_id,
        "product_name": product_name,
        "alert": "Stock low"
    }

    response = client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    print("SQS MessageId:", response['MessageId'])
