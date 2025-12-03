---
title : "StorePlanningApp  Function"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---

Trong bước này, bạn sẽ tạo **StorePlanningApp Lambda Function** - ứng dụng xử lý logic lập kế hoạch cho hệ thống cửa hàng. Function này sẽ nhận messages từ SQS Queue, thực hiện phân tích dữ liệu từ Athena và tạo ra các chiến lược lập kế hoạch cung ứng.

## Tổng quan StorePlanningApp Lambda Function

StorePlanningApp đóng vai trò quan trọng trong kiến trúc analytics:

- **Message Consumer**: Nhận và xử lý messages từ SQS Store_Queue
- **Data Analytics**: Query dữ liệu từ Athena/Glue để phân tích tồn kho
- **Planning Logic**: Tính toán nhu cầu và tạo kế hoạch cung ứng
- **Result Storage**: Lưu kết quả phân tích vào S3 bucket

## Hướng dẫn từng bước

### Bước 1: Navigate to Lambda Console

1. Trong thanh tìm kiếm AWS Console
2. Nhập **"lambda"**
3. Chọn **"Lambda"** từ kết quả tìm kiếm

![Navigate to Lambda](/images/22.png)

### Bước 2: Create New Function

1. Nhấp vào nút **"Create function"**
2. **Function name**: Đặt tên `StorePlanningApp`
3. **Runtime**: Chọn **"Python 3.13"**
4. Các cấu hình khác giữ mặc định
5. Nhấp **"Create function"**

![Create Planning Lambda](/images/23.png)

{{% notice info %}}
**StorePlanningApp**: Function này sẽ chứa logic phức tạp hơn StoreApp, bao gồm Athena queries và planning algorithms.
{{% /notice %}}

### Bước 3: Deploy Function Code

1. Trong giao diện Lambda code của "StorePlanningApp"
2. Thực hiện các bước tương tự như đã làm với "StoreApp":
   - Tạo file `function.py` 
   - Cấu hình handler thành `function.lambda_handler`
3. Copy và paste code từ link sau: [📁 planning-function.py](/downloads/planning-function.py)
4. Nhấp **"Deploy"** để deploy code

![Deploy Planning Code](/images/24.png)

{{% notice download %}}
**📁 Source Code Required**: Copy nội dung từ link [planning-function.py](/downloads/planning-function.py) và paste vào file `function.py` trong Lambda editor.
{{% /notice %}}

### Bước 4: Configure Environment Variables

1. Navigate sang phần **"Configuration"**
2. Chọn **"Environment variables"** 
3. Nhấp vào **"Edit"**

Thêm 4 environment variables sau:

| Key | Value | Description |
|-----|--------|-------------|
| `glue_db` | `conversion_db` | Tên Glue database |
| `glue_table` | `conversion_table` | Tên Glue table |
| `output_bucket` | `s3://consumption-bucket-yourname/` | S3 bucket output |
| `queue_url` | `https://sqs.ap-southeast-1.amazonaws.com/yourID/Store_Queue` | SQS Queue URL |

![Configure Environment Variables](/images/26.png)

{{% notice warning %}}
**Replace Information**: 
- Thay `yourname` trong bucket name bằng tên của bạn
- Thay `yourID` trong queue URL bằng AWS Account ID của bạn
{{% /notice %}}

### Bước 5: Configure Timeout

1. Vẫn trong phần **"Configuration"**
2. Chọn **"General configuration"**
3. Nhấp vào **"Edit"**

![Navigate General Config](/images/27.png)

4. Đặt **Timeout** thành **"2 min"** (120 seconds)
5. Nhấp **"Save"** để lưu cấu hình

![Set Timeout](/images/28.png)

{{% notice tip %}}
**Why 2 minutes timeout?**: StorePlanningApp cần thời gian để query Athena và xử lý dữ liệu, timeout dài hơn đảm bảo function không bị terminate sớm.
{{% /notice %}}

### Bước 6: Configure IAM Permissions

1. Navigate về **IAM Console**
2. Trong thanh tìm kiếm, nhập **"store"** 
3. Tìm và chọn role **"StorePlanningApp-role-xxxxx"**

![Find Planning Role](/images/21_5.png)

4. Nhấp **"Add permissions"** → **"Attach policies"**

![Add Permissions](/images/21_6.png)

5. Thêm các policies sau (tìm kiếm và attach từng policy):
   - ✅ **AmazonAthenaFullAccess** 
   - ✅ **AmazonS3FullAccess**
   - ✅ **AmazonSQSFullAccess** 
   - ✅ **AWSGlueConsoleFullAccess**

![Attach Policies](/images/21_7.png)

{{% notice info %}}
**IAM Permissions Explained**:
- **Athena**: Query dữ liệu từ data lake
- **S3**: Read/write result files
- **SQS**: Receive messages từ queue
- **Glue**: Access metadata catalog
{{% /notice %}}

### Bước 7: Test Lambda Function

1. Quay lại Lambda **"StorePlanningApp"**
2. Navigate tới phần **"Test"**
3. Tạo test event với tên **"test"**
4. Nhấp nút **"Test"** để thực hiện

![Create Test Event](/images/29.png)

### Bước 8: Verify Test Results

Sau khi test thành công, bạn sẽ thấy:

- ✅ **Execution result**: succeeded
- ✅ **Function logs**: Thông tin xử lý chi tiết
- ✅ **Duration**: Thời gian thực thi
- ✅ **Memory used**: Resource consumption

![Test Results](/images/30.png)

## Verify Function Operation

Sau khi hoàn thành các bước trên, StorePlanningApp Lambda function có:

✅ **Runtime**: Python 3.13  
✅ **Handler**: function.lambda_handler  
✅ **Source Code**: Planning logic deployed  
✅ **Environment Variables**: 4 variables configured  
✅ **Timeout**: 2 minutes  
✅ **IAM Permissions**: 4 policies attached  
✅ **Test Status**: Successfully executed  

{{% notice success %}}
**StorePlanningApp Complete!** Lambda function đã được tạo, cấu hình và test thành công. Function sẵn sàng xử lý planning logic từ SQS messages.
{{% /notice %}}

## Tóm tắt

StorePlanningApp Lambda function hiện đã:

- **Receives and processes** messages từ SQS Queue
- **Queries data** từ Athena cho analytics  
- **Executes planning logic** dựa trên inventory data
- **Stores results** vào S3 bucket
- **Ready to scale** với message volume

Function này là thành phần cốt lõi trong store planning và analytics pipeline của chúng ta!