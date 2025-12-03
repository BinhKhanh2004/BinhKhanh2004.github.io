import os
import json
import random
import boto3
import time
firehose_client = boto3.client('firehose')
timestamp = time.time()

def lambda_handler(event, context):
    
    DELIVERY_STREAM = os.environ['delivery_stream']
    
    store_list = []
    
    for i in range(10):  # Mô phỏng 10 cửa hàng
        
        store_id = f"STORE_{i+1}"
        product_id = f"PRD_{random.randint(1, 5)}"
        product_name = random.choice(["Rau cải", "Thịt gà", "Sữa tươi", "Cơm hộp", "Bánh mì"])
        
        current_stock = random.randint(0, 20)
        threshold_level = random.randint(5, 15)
        
        # Xác định trạng thái thiếu hàng
        is_stock_low = current_stock < threshold_level
        
        json_data = {
            "store_id": store_id,
            "product_id": product_id,
            "product_name": product_name,
            "current_stock": current_stock,
            "threshold_level": threshold_level,
            "is_stock_low": is_stock_low,
            "check_timestamp": int(timestamp),
            "notification_sent": False,
            "restock_status": "chưa xử lý"
        }

        response = firehose_client.put_record(
            DeliveryStreamName=DELIVERY_STREAM,
            Record={"Data": json.dumps(json_data)}
        )
        
        store_list.append(json_data)
    
    return store_list
