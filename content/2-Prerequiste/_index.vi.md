---
title : "Chuẩn bị"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

Trong module này, bạn sẽ chuẩn bị các thành phần hạ tầng cơ bản cần thiết cho pipeline streaming analytics của chúng ta. Những thành phần này sẽ phục vụ như xương sống cho việc lưu trữ, xử lý và phân tích dữ liệu trong suốt workshop.

## Tổng quan Thành phần Hạ tầng

Trước khi chúng ta có thể bắt đầu streaming và phân tích dữ liệu hàng tồn kho cửa hàng, chúng ta cần thiết lập:

1. **S3 Consumption Bucket** - Lưu trữ data lake cho các bản ghi hàng tồn kho được stream
2. **IAM Role cho Kinesis Data Firehose** - Quyền để giao dữ liệu đến S3
3. **Conversion Database** - Cơ sở dữ liệu AWS Glue Data Catalog để tổ chức dữ liệu của chúng ta
4. **Conversion Table** - Cấu trúc bảng Glue mà Athena sẽ sử dụng để truy vấn dữ liệu hàng tồn kho

## Tại sao các Thành phần này Quan trọng

### S3 Consumption Bucket
Hoạt động như **data lake** của bạn, nơi tất cả dữ liệu hàng tồn kho streaming từ các cửa hàng sẽ được lưu trữ. Bucket này phục vụ như kho lưu trữ trung tâm mà Amazon Athena sẽ truy vấn để phân tích.

### IAM Role cho Firehose
Đảm bảo **giao dữ liệu an toàn** từ Kinesis Data Firehose đến S3 bucket của bạn. Nếu không có quyền phù hợp, pipeline streaming không thể hoạt động.

### Conversion Database & Table
Tạo **metadata catalog** trong AWS Glue Data Catalog để định nghĩa schema cho dữ liệu hàng tồn kho của bạn. Amazon Athena sử dụng Glue catalog này để hiểu cấu trúc dữ liệu S3 của bạn, cho phép thực hiện SQL queries trên các bản ghi JSON hàng tồn kho thô. Database phục vụ như container logic, trong khi định nghĩa table ánh xạ các trường JSON thành các cột có thể truy vấn.

{{% notice info %}}
**Thời gian Chuẩn bị**: Module này sẽ mất khoảng 15-20 phút để hoàn thành tất cả các tác vụ thiết lập.
{{% /notice %}}

{{% notice warning %}}
**Quan trọng**: Hoàn thành tất cả các bước chuẩn bị theo thứ tự. Mỗi thành phần phụ thuộc vào việc các thành phần trước đó được cấu hình đúng cách.
{{% /notice %}}

### Nội dung Workshop
  - [Tạo S3 Consumption Bucket](2.1-create-s3-bucket/)  
  - [Tạo IAM Role cho Kinesis Data Firehose](2.2-create-firehose-role/)  
  - [Tạo Conversion Database trong AWS Glue Data Catalog](2.3-create-glue-database/)  
  - [Tạo Conversion Table trong AWS Glue Data Catalog](2.4-create-glue-table/)

Khi bạn hoàn thành giai đoạn chuẩn bị này, bạn sẽ có nền tảng vững chắc để xây dựng pipeline streaming analytics cho quản lý hàng tồn kho cửa hàng.