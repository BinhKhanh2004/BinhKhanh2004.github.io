import os
import json
import boto3

def lambda_handler(event, context):
    
    QUEUE_URL = os.environ['queue_url']
    
    # SQS client
    client = boto3.client('sqs')
    
    # Nhận tối đa 10 tin nhắn trong hàng đợi
    response = client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5
    )
    
    for message in response.get('Messages', []):
        body = json.loads(message['Body'])
        
        store_id = body.get('store_id')
        product_name = body.get('product_name')
        
        print(f"🚚 Đã gửi hàng tiếp tế cho cửa hàng {store_id} — sản phẩm thiếu: {product_name}")
        
        # Xóa tin nhắn đã xử lý khỏi hàng đợi
        receipt_handle = message['ReceiptHandle']
        client.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
    
    processed_messages = len(response.get('Messages', []))
    
    if processed_messages == 0:
        return f"📭 Không có cảnh báo tồn kho nào. Số tin đã xử lý: {processed_messages}"
    else:
        return f"📦 Số lượng cảnh báo đã xử lý: {processed_messages}"
