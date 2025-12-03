---
title : "Data Firehose Stream"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

Trong module này, bạn sẽ tạo Kinesis Data Firehose delivery stream - thành phần cốt lõi của streaming analytics pipeline. Firehose sẽ thu thập dữ liệu inventory từ StoreApp và tự động ghi vào S3 consumption bucket với format được tối ưu hóa cho analytics.

## Kinesis Data Firehose Overview

Amazon Kinesis Data Firehose là fully-managed service giúp bạn:

- **Tự động thu thập và chuyển đổi** streaming data từ nhiều nguồn khác nhau
- **Ghi dữ liệu vào data lake** với format tối ưu (Parquet) cho analytics
- **Phân vùng động (Dynamic Partitioning)** để tối ưu hiệu suất truy vấn Athena
- **Chuyển đổi format** từ JSON thành Parquet tự động
- **Retry và error handling** đảm bảo data reliability

### Architecture Integration

Trong pipeline của chúng ta:
1. **StoreApp** → streams inventory data → **Firehose**
2. **Firehose** → converts JSON to Parquet → **S3 Bucket**
3. **Firehose** → updates metadata → **Glue Data Catalog** 
4. **Athena** → queries optimized data → **Analytics insights**

## Step-by-Step Instructions

### Step 1: Navigate to Kinesis Console

1. Vào thanh tìm kiếm AWS Console
2. Search **"Kinesis"**
3. Nhấp vào **"Kinesis"**

![Navigate to Kinesis](/images/1.png)

### Step 2: Access Data Firehose

1. Trong giao diện **"Get started"**, chọn **"Amazon Data Firehose"**
2. Nhấp vào **"Create Firehose stream"** để bắt đầu tạo một stream firehose

![Access Data Firehose](/images/2.png)

### Step 3: Configure Source and Destination

1. **Source**: Chọn **"Direct put"**
2. **Destination**: Chọn **"Amazon S3"**
3. **Firehose stream name**: Đặt tên `SI-Firehose`

![Configure Source and Destination](/images/3.png)

{{% notice info %}}
**Direct put**: Có nghĩa là applications sẽ gửi dữ liệu trực tiếp vào Firehose stream thay vì thông qua Kinesis Data Stream trung gian.
{{% /notice %}}

### Step 4: Enable Record Format Conversion

1. Ở phần **"Transform and convert records"** → **"Convert record format"**
2. Bật **"Enable record format conversion"**
3. Sau khi enable, sẽ hiện thêm các chi tiết bổ sung:
   - **AWS Glue Region**: Chọn vùng giống với vùng đang sử dụng (Singapore)
   - **AWS Glue Database**: Chọn `conversion_db`
   - **AWS Glue Table**: Chọn `conversion_table`

![Enable Record Format Conversion](/images/4.png)

{{% notice tip %}}
**Format Conversion**: Việc chuyển đổi từ JSON sang Parquet giúp giảm kích thước file lên đến 80% và tăng tốc độ truy vấn Athena đáng kể.
{{% /notice %}}

### Step 5: Configure S3 Destination and Dynamic Partitioning

1. **Destination Settings** → **S3 bucket**: Chọn consumption bucket đã tạo ở phần 2.1
2. **Dynamic partitioning**: Bật **"Enabled"**
3. **Inline parsing for JSON**: Bật **"Enabled"**

![Configure S3 and Dynamic Partitioning](/images/5.png)

### Step 6: Add Dynamic Partitioning Keys

1. Ở phần **"Dynamic partitioning keys"**, add các keys như trong ảnh
2. Sau khi add các keys, phần **"S3 bucket prefix"** sẽ được tự động điền
3. Để đảm bảo, copy và paste đoạn sau vào **S3 bucket prefix**:
   ```
   store-data/store_id=!{partitionKeyFromQuery:store_id}/!{partitionKeyFromQuery:year}/!{partitionKeyFromQuery:month}/!{partitionKeyFromQuery:day}/!{partitionKeyFromQuery:hour}/
   ```
4. **S3 bucket error output prefix**: Nhập `error`
5. **Retry duration**: Nhập `60` seconds

![Add Dynamic Partitioning Keys](/images/6.png)

{{% notice info %}}
**Dynamic Partitioning**: Tự động tổ chức dữ liệu theo store_id và timestamp, giúp Athena truy vấn nhanh hơn bằng cách chỉ scan các partition cần thiết.
{{% /notice %}}

### Step 7: Configure IAM Role and Create Stream

1. Mở rộng phần **"Advanced settings"**
2. **Service access**: Chọn **"Choose existing IAM role"**
3. Chọn IAM role **"FirehoseWorkshop"** đã tạo từ bước trước
4. Kéo xuống và nhấp **"Create firehose stream"**

![Configure IAM and Create](/images/7.png)

### Step 8: Verification

Sau khi hoàn thành thiết lập, bạn sẽ thấy Firehose stream `SI-Firehose` đã được tạo thành công với status **"Active"**.

![Firehose Stream Created](/images/8.png)

## Verification Checklist

Xác nhận các cấu hình sau đã được thiết lập đúng:

✅ **Source**: Direct put  
✅ **Destination**: Amazon S3 (consumption bucket của bạn)  
✅ **Format conversion**: Enabled (JSON → Parquet)  
✅ **Glue integration**: conversion_db.conversion_table  
✅ **Dynamic partitioning**: Enabled với các keys phù hợp  
✅ **IAM role**: FirehoseWorkshop  
✅ **Status**: Active  

{{% notice success %}}
**Hoàn thành!** Kinesis Data Firehose stream đã sẵn sàng nhận dữ liệu streaming từ StoreApp và tự động ghi vào data lake với format được tối ưu hóa.
{{% /notice %}}

{{% notice warning %}}
**Lưu ý về Costs**: Firehose stream đang active sẽ phát sinh chi phí dựa trên lượng dữ liệu được xử lý. Nhớ cleanup resources sau khi hoàn thành workshop.
{{% /notice %}}

## What's Next?

Firehose stream của bạn đã sẵn sàng. Trong bước tiếp theo, chúng ta sẽ tạo Lambda function để xử lý analytics và tạo StoreApp để bắt đầu streaming dữ liệu inventory.

Tiếp tục với: [**Create Store Analytics Lambda Function**](../4-create-lambda/)