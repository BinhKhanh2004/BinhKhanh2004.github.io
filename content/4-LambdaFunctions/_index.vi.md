---
title : "Lambda Functions"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

Trong phần này, bạn sẽ tìm hiểu về **AWS Lambda Functions** và vai trò của nó trong kiến trúc streaming analytics. Lambda sẽ đóng vai trò quan trọng trong việc xử lý dữ liệu real-time từ các cửa hàng và gửi thông báo tới hệ thống quản lý xe chở hàng.

## Tổng quan về AWS Lambda

AWS Lambda là một dịch vụ điện toán **serverless** cho phép bạn chạy code mà không cần cung cấp hoặc quản lý máy chủ. Lambda tự động mở rộng quy mô ứng dụng bằng cách chạy code để phản hồi với mỗi trigger, tự động quản lý các tài nguyên điện toán cơ bản.

### Tại sao sử dụng Lambda trong Streaming Data Pipeline?

Trong bối cảnh hệ thống quản lý lương thực cửa hàng của chúng ta, Lambda đóng vai trò như một **bộ xử lý dữ liệu thời gian thực**:

- **Trình tạo dữ liệu**: Tạo dữ liệu mô phỏng tồn kho từ nhiều cửa hàng khác nhau
- **Tích hợp streaming**: Gửi dữ liệu trực tiếp tới Kinesis Data Firehose
- **Điều khiển bằng sự kiện**: Có thể được kích hoạt thủ công hoặc theo lịch trình
- **Định dạng JSON**: Tạo dữ liệu với cấu trúc JSON tương thích với schema của bảng Glue

## Chức năng của StoreApp Lambda Function

StoreApp Lambda function sẽ mô phỏng các cửa hàng bán lẻ gửi thông tin tồn kho như:

✅ **Store ID và vị trí**: Định danh và địa điểm của cửa hàng  
✅ **Thông tin sản phẩm**: ID, tên, danh mục sản phẩm  
✅ **Mức tồn kho**: So sánh tồn kho hiện tại với ngưỡng tối thiểu  
✅ **Timestamp**: Dấu thời gian để theo dõi real-time  

{{% notice info %}}
**Lambda trong Streaming Analytics**: Lambda function đóng vai trò trung gian quan trọng, nhận dữ liệu từ nguồn và chuyển đổi trước khi gửi tới Kinesis Data Firehose.
{{% /notice %}}

## Ưu điểm của Lambda trong hệ thống

### ⚡ **Serverless Computing**
- Không cần quản lý infrastructure
- AWS xử lý tất cả việc provisioning và scaling
- Tập trung vào business logic thay vì quản lý server

### 📈 **Auto-scaling**
- Tự động mở rộng theo lưu lượng
- Xử lý từ vài request đến hàng nghìn request/giây
- Không cần cấu hình capacity planning

### 💰 **Cost-effective**
- Chỉ trả tiền khi code thực thi
- Không có chi phí khi idle
- Mô hình pricing theo request và compute time

### 🔄 **Event-driven**
- Phản ứng ngay lập tức với events
- Tích hợp với nhiều AWS services
- Hỗ trợ real-time data processing

## Chuẩn bị cho các bước tiếp theo

Trong các phần tiếp theo, chúng ta sẽ:

1. **[Tạo và cấu hình StoreApp Lambda Function](../4.1-create-lambda/)** 
   - Tạo function với Python 3.13 runtime
   - Cấu hình handler và environment variables

2. **[Cấu hình quyền và test Lambda Function](../4.2-configure-test-lambda/)**
   - Thêm IAM permissions cho Kinesis Data Firehose
   - Tạo và chạy test event
   - Xác minh kết quả trong S3

{{% notice warning %}}
**Lưu ý quan trọng**: Lambda function trong workshop này sẽ được kích hoạt **thủ công** để bạn có thể quan sát và hiểu rõ từng bước xử lý dữ liệu trong pipeline.
{{% /notice %}}

## Tổng kết

AWS Lambda là thành phần cốt lõi trong kiến trúc streaming analytics của chúng ta. Nó cung cấp:

- **Khả năng xử lý real-time** cho dữ liệu từ cửa hàng
- **Tích hợp seamless** với Kinesis Data Firehose  
- **Serverless architecture** giúp giảm complexity
- **Cost optimization** với pay-per-use model

Hãy bắt đầu với việc tạo StoreApp Lambda Function trong bước tiếp theo!