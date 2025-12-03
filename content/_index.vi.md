---
title : "Phân tích Streaming cho Quản lý Hàng tồn kho Cửa hàng"
weight : 2
chapter : false
---

# Giới thiệu

Trong bài thực hành này, bạn sẽ xây dựng một **hệ thống phân tích streaming** để giám sát mức hàng tồn kho của cửa hàng và điều phối việc điều động xe tải giao hàng để bổ sung hàng hóa.

Dữ liệu sản phẩm của cửa hàng được đưa vào thông qua **StoreApp** vào **Amazon Kinesis Data Firehose**, ứng dụng này sẽ streaming dữ liệu đến một **S3 bucket**. Bạn sẽ **thủ công gọi một Lambda function** để truy vấn dữ liệu bằng **Amazon Athena**, phân tích mức hàng tồn kho, và phát hiện những cửa hàng nào cần bổ sung hàng cho các sản phẩm cụ thể.

Khi Lambda function được thực thi, các cảnh báo hàng tồn kho thấp sẽ được gửi đến **Amazon SQS Queue**, mà **StoreTruckApp** theo dõi để điều động xe tải giao hàng đến các địa điểm cửa hàng phù hợp.

## Mục tiêu Học tập
- Hiểu cách đưa dữ liệu cửa hàng thời gian thực bằng Amazon Kinesis Data Firehose
- Thực hành tạo và **thủ công kích hoạt Lambda functions** để xử lý phân tích hàng tồn kho
- Truy vấn dữ liệu streaming được lưu trữ trong S3 bằng Amazon Athena
- Gửi tin nhắn điều phối giao hàng qua Amazon SQS
- Xây dựng một pipeline phân tích streaming từ đầu đến cuối cho hoạt động bán lẻ

## Kiến trúc Tổng thể
![Architecture Diagram](/images/store-inventory-pipeline.png)

1. **Dữ liệu sản phẩm** → **StoreApp** streaming đến **Amazon Kinesis Data Firehose**
2. **Kinesis Data Firehose** → lưu trữ dữ liệu trong **S3 bucket** (vùng tiêu thụ)
3. **Amazon Athena** → truy vấn dữ liệu S3 để phân tích hàng tồn kho
4. Người dùng **thủ công gọi Lambda** → **StorePlanningApp** xử lý mức hàng tồn kho
5. **Lambda** → phát hiện các cửa hàng có hàng tồn kho thấp và gửi cảnh báo đến **Amazon SQS Queue**
6. **StoreTruckApp** → tiêu thụ tin nhắn SQS và điều phối xe tải **Giao hàng**
7. **Xe tải giao hàng** → bổ sung hàng hóa cho các cửa hàng dựa trên nhu cầu hàng tồn kho

{{% notice info %}}
**Điểm Quan trọng**: Không giống như các hệ thống tự động hoàn toàn, bạn sẽ thủ công kích hoạt Lambda function để xử lý dữ liệu hàng tồn kho và điều phối giao hàng. Điều này giúp bạn có quyền kiểm soát trực tiếp đối với pipeline phân tích.
{{% /notice %}}