---
title : "Tạo StoreTruckApp và hoàn thành Pipeline"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 4.5 </b> "
---

Trong bước cuối cùng này, chúng ta sẽ tạo **StoreTruckApp Lambda Function** và **Truck_Queue** để hoàn thiện toàn bộ streaming analytics pipeline. StoreTruckApp sẽ xử lý thông tin xe chở hàng và điều phối việc giao hàng dựa trên kết quả phân tích từ StorePlanningApp.

## Tổng quan StoreTruckApp

StoreTruckApp là thành phần cuối cùng trong kiến trúc streaming analytics:

- **Truck Management**: Quản lý xe chở hàng
- **Delivery Coordination**: Điều phối việc giao hàng dựa trên planning results
- **Route Optimization**: Tối ưu hóa tuyến đường giao hàng
- **Status Tracking**: Theo dõi trạng thái giao hàng real-time

## Hướng dẫn từng bước

### Bước 1: Create StoreTruckApp Lambda Function

1. Vào **Lambda Console**
2. Nhấp **"Create function"**
3. Cấu hình function với các settings giống như 2 function trước:
   - **Function name**: `StoreTruckApp`
   - **Runtime**: **Python 3.13**
   - **Handler**: `function.lambda_handler`
4. Nhấp **"Create function"**

![Create StoreTruckApp](/images/31.png)

{{% notice info %}}
**StoreTruckApp Purpose**: Function này sẽ nhận thông tin về nhu cầu giao hàng và điều phối các xe chở hàng một cách tối ưu.
{{% /notice %}}

### Bước 2: Deploy Source Code

1. Trong giao diện code của StoreTruckApp
2. Tạo file `function.py` 
3. Copy và paste code từ link sau: [📁 truck-app-function.py](/downloads/truck-app-function.py)
4. Nhấp **"Deploy"** để deploy code

![Deploy Truck App Code](/images/32.png)

{{% notice download %}}
**📁 Source Code Required**: Copy nội dung từ link [truck-app-function.py](/downloads/truck-app-function.py) và paste vào file `function.py`.
{{% /notice %}}

### Bước 3: Configure IAM Permissions

1. Navigate tới **IAM Console**
2. Trong thanh tìm kiếm, tìm kiếm role của **"StoreTruckApp"**
3. Chọn role **"StoreTruckApp-role-xxxxx"**

![Find Truck App Role](/images/32_2.png)

4. **Add permissions** → **"Attach policies"**
5. Attach các policies sau:
   - ✅ **AmazonAthenaFullAccess**
   - ✅ **AmazonS3FullAccess** 
   - ✅ **AmazonSQSFullAccess**
   - ✅ **AWSGlueConsoleFullAccess**

![Attach Truck App Policies](/images/32_4.png)

{{% notice info %}}
**Same Permissions**: StoreTruckApp cần cùng các permissions như StorePlanningApp để có thể query data và gửi message.
{{% /notice %}}

### Bước 4: Configure Timeout

1. Quay trở lại Lambda **"StoreTruckApp"**
2. Vào phần **"Configuration"** → **"General configuration"**
3. Nhấp **"Edit"**

![Navigate to General Config](/images/32_5.png)

4. Đặt **Timeout** thành **"2 min"** (120 seconds)
5. Nhấp **"Save"** để lưu

![Set Truck App Timeout](/images/32_6.png)

### Bước 5: Create Truck_Queue

1. Navigate tới **Amazon SQS Console**
2. Nhấp **"Create queue"**
3. Tạo queue với cùng cấu hình như trước:
   - **Queue name**: `Truck_Queue`
   - **Queue type**: **Standard**
   - Các settings khác giữ mặc định
4. Nhấp **"Create queue"**

![Create Truck Queue](/images/33.png)

{{% notice tip %}}
**Truck_Queue Role**: Queue này sẽ nhận delivery request messages và trigger StoreTruckApp để xử lý.
{{% /notice %}}

### Bước 6: Configure Environment Variables

1. Quay lại Lambda **"StoreTruckApp"**
2. Navigate tới **"Configuration"** → **"Environment variables"**
3. Nhấp **"Edit"**
4. Thêm environment variable:
   - **Key**: `queue_url`
   - **Value**: `https://sqs.ap-southeast-1.amazonaws.com/yourID/Truck_Queue`

![Configure Truck App Environment](/images/34.png)

{{% notice warning %}}
**Replace yourID**: Nhớ thay `yourID` bằng AWS Account ID thực tế của bạn trong Queue URL.
{{% /notice %}}

### Bước 7: Test StoreTruckApp Function

1. Vào phần **"Test"** của StoreTruckApp
2. Tạo test event với tên **"test"**
3. Nhấp nút **"Test"** để thực hiện

![Test Truck App](/images/35.png)

## Verify Complete Pipeline

Sau khi hoàn thành tất cả các bước, hệ thống streaming analytics có:

✅ **Data Ingestion**: StoreApp + Kinesis Firehose + S3  
✅ **Data Cataloging**: AWS Glue Database & Table  
✅ **Data Analytics**: Athena queries từ StorePlanningApp  
✅ **Message Queuing**: Store_Queue + Truck_Queue  
✅ **Business Logic**: StorePlanningApp + StoreTruckApp  
✅ **End-to-End Flow**: Từ stores đến delivery trucks  

{{% notice success %}}
**🎉 Workshop Complete!** Bạn đã hoàn thành thành công workshop Streaming Ingestion & Analytics với kiến trúc serverless hoàn chỉnh trên AWS!
{{% /notice %}}

## Workshop Summary

### What we have built:

🏪 **Real-time Data Pipeline**: Thu thập dữ liệu real-time từ stores  
📊 **Serverless Analytics**: Xử lý và phân tích dữ liệu không cần server management  
🚛 **Intelligent Routing**: Điều phối delivery trucks dựa trên data analysis  
⚡ **Event-driven Architecture**: Toàn bộ hệ thống hoạt động theo events  
💰 **Cost Optimized**: Chỉ trả tiền khi có data processing  

### AWS Services Used:

- **AWS Lambda**: Serverless compute cho business logic
- **Amazon Kinesis Data Firehose**: Streaming data ingestion  
- **Amazon S3**: Data lake storage
- **AWS Glue**: Data cataloging và ETL
- **Amazon Athena**: Serverless analytics
- **Amazon SQS**: Message queuing
- **IAM**: Security và permissions

### Knowledge Gained:

✅ **Streaming Data Architecture** design patterns  
✅ **Serverless Computing** với AWS Lambda  
✅ **Real-time Analytics** với Kinesis và Athena  
✅ **Event-driven Systems** với SQS  
✅ **Data Lake Architecture** với S3 và Glue  
✅ **Security Best Practices** với IAM  

## Next Steps

Bây giờ bạn có thể:

1. **Extend Pipeline**: Thêm các Lambda functions khác cho advanced analytics
2. **Add Monitoring**: Sử dụng CloudWatch để monitor pipeline
3. **Implement Dashboard**: Tạo visualization với QuickSight
4. **Scale Up**: Apply pattern này cho production workloads
5. **Cost Optimization**: Fine-tune resources cho cost efficiency

{{% notice tip %}}
**Continue Learning**: Hãy thử experiment với các AWS services khác như EventBridge, Step Functions, hoặc Elasticsearch để extend pipeline này!
{{% /notice %}}

---

**🎯 Congratulations!** Bạn đã thành thạo cách xây dựng một complete streaming analytics pipeline trên AWS!