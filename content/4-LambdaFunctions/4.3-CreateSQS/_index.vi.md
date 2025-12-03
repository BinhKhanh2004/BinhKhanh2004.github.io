---
title : "Tạo SQS Queue"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 4.3 </b> "
---

Trong bước này, bạn sẽ tạo một **Amazon SQS Queue** - một message queue để xử lý các yêu cầu lập kế hoạch từ hệ thống cửa hàng. SQS Queue sẽ đóng vai trò như một bộ đệm giữa các thành phần trong kiến trúc streaming analytics.

## Tổng quan về Amazon SQS

Amazon Simple Queue Service (SQS) là một dịch vụ message queuing được quản lý hoàn toàn cho phép bạn tách biệt và mở rộng quy mô các microservices, hệ thống phân tán và ứng dụng serverless.

### Vai trò của SQS trong hệ thống của chúng ta

Trong kiến trúc Store Planning của chúng ta, SQS Queue sẽ:

- **Message Buffer**: Lưu trữ tạm thời các message từ hệ thống
- **Decoupling**: Tách biệt data producers khỏi consumers
- **Reliability**: Đảm bảo messages không bị mất trong quá trình xử lý
- **Scalability**: Tự động mở rộng quy mô theo khối lượng message

{{% notice info %}}
**SQS trong Streaming Pipeline**: Queue sẽ nhận messages từ các nguồn khác nhau và kích hoạt Lambda functions để xử lý logic lập kế hoạch.
{{% /notice %}}

## Hướng dẫn từng bước

### Bước 1: Navigate to SQS Console

1. Trong thanh tìm kiếm AWS Console
2. Nhập **"sqs"**
3. Chọn **"Simple Queue Service"** từ kết quả tìm kiếm

![Navigate to SQS](/images/21_1.png)

### Bước 2: Create New Queue

1. Trong giao diện SQS Console
2. Nhấp vào nút **"Create queue"**

![Create Queue](/images/21_2.png)

### Bước 3: Configure Queue Settings

1. **Queue name**: Đặt tên `Store_Queue`
2. **Queue type**: Giữ mặc định **"Standard"**
3. Để các cấu hình khác ở settings mặc định
4. Nhấp **"Create queue"** để hoàn thành

![Configure Queue](/images/21_3.png)

{{% notice tip %}}
**Standard vs FIFO Queue**: Standard queue cung cấp high throughput và at-least-once delivery, phù hợp cho use case streaming analytics của chúng ta.
{{% /notice %}}

## Xác minh tạo Queue

Sau khi tạo thành công, bạn sẽ thấy:

✅ **Queue Name**: Store_Queue  
✅ **Queue Type**: Standard  
✅ **Status**: Active  
✅ **Queue URL**: Tự động được tạo (sẽ được sử dụng trong bước tiếp theo)  

{{% notice success %}}
**SQS Queue Created!** Store_Queue đã được tạo thành công và sẵn sàng nhận messages từ hệ thống.
{{% /notice %}}

## Queue URL và Integration

Queue URL sẽ có định dạng:
```
https://sqs.ap-southeast-1.amazonaws.com/[YOUR-ACCOUNT-ID]/Store_Queue
```

{{% notice warning %}}
**Note Queue URL**: Bạn sẽ cần copy Queue URL này để cấu hình trong Lambda function ở bước tiếp theo. URL này là định danh duy nhất cho queue của bạn.
{{% /notice %}}

## Chuẩn bị cho bước tiếp theo

Store_Queue hiện đã sẵn sàng để:

- **Nhận messages** từ các data sources
- **Kích hoạt Lambda function** khi có messages mới đến
- **Đảm bảo độ tin cậy** trong việc xử lý message

{{% notice info %}}
**Bước tiếp theo**: Trong bước tiếp theo, chúng ta sẽ tạo Lambda function "StorePlanningApp" sẽ được kích hoạt bởi messages từ Store_Queue này.
{{% /notice %}}

## Tóm tắt

Amazon SQS Store_Queue đã được thiết lập thành công với:

- **Message queuing đáng tin cậy** cho hệ thống lập kế hoạch cửa hàng
- **Standard queue type** cho high throughput
- **Sẵn sàng tích hợp** với Lambda function
- **Kiến trúc có thể mở rộng** hỗ trợ tăng trưởng trong tương lai