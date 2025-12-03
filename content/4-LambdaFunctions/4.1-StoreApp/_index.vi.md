---
title : "Tạo StoreApp Function"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

Trong bước này, bạn sẽ tạo **StoreApp Lambda function** - ứng dụng mô phỏng các cửa hàng gửi dữ liệu tồn kho real-time vào Kinesis Data Firehose stream. Lambda function này sẽ tạo và truyền dữ liệu tồn kho của các cửa hàng để phục vụ cho analytics pipeline.

## Tổng quan về StoreApp Lambda Function

StoreApp Lambda function đóng vai trò quan trọng trong kiến trúc streaming analytics:

- **Data Generator**: Tạo dữ liệu tồn kho mô phỏng từ nhiều cửa hàng khác nhau
- **Streaming Integration**: Gửi dữ liệu trực tiếp vào Kinesis Data Firehose
- **Event-Driven**: Có thể được kích hoạt thủ công hoặc theo lịch trình
- **JSON Format**: Tạo dữ liệu với cấu trúc JSON phù hợp với Glue table schema

### Mục đích của Function
StoreApp sẽ mô phỏng việc các cửa hàng bán lẻ gửi thông tin tồn kho như:
- Store ID và location
- Thông tin sản phẩm (ID, tên, danh mục)
- Mức tồn kho (so sánh hiện tại với ngưỡng tối thiểu)
- Timestamps cho việc theo dõi real-time

## Hướng dẫn từng bước

### Bước 1: Navigate to Lambda Console

1. Trong thanh tìm kiếm AWS Console
2. Nhập **"lambda"**
3. Chọn **"Lambda"** từ kết quả tìm kiếm

![Navigate to Lambda](/images/9.png)

### Bước 2: Create New Function

1. Nhấp vào nút **"Create function"** ở góc trên bên phải

![Create Function](/images/10.png)

### Bước 3: Configure Function Settings

1. **Function name**: Đặt tên `StoreApp`
2. **Runtime**: Chọn **"Python 3.13"**
3. Các settings khác để mặc định
4. Nhấp **"Create function"** để qua bước tiếp theo

![Configure Function Settings](/images/11.png)

{{% notice info %}}
**Python 3.13**: Version mới nhất với hiệu suất được cải thiện và hỗ trợ tốt hơn cho AWS SDK (boto3).
{{% /notice %}}

### Bước 4: Edit Runtime Settings

1. Sau khi tạo xong function, ở phần **"Code"**
2. Kéo xuống mục **"Runtime settings"** 
3. Nhấp vào **"Edit"**

![Edit Runtime Settings](/images/12_1.png)

### Bước 5: Update Handler Configuration

1. Trong giao diện mới hiện ra:
   - **Runtime**: Chọn **"Python 3.13"**
   - **Handler**: Nhập `function.lambda_handler`
2. Nhấp **"Save"** để lưu cấu hình

![Update Handler](/images/12_2.png)

{{% notice tip %}}
**Handler**: `function.lambda_handler` có nghĩa Lambda sẽ gọi hàm `lambda_handler()` trong file `function.py`.
{{% /notice %}}

### Bước 6: Create Function Code File

1. Ở phần **"Code"**, tìm và nhấp vào biểu tượng tạo file mới (được tô dấu trong ảnh)
2. Đặt tên cho file mới: `function.py`
3. Copy nội dung từ link sau và paste vào file: [📁 storeapp-function.py](/downloads/storeapp-function.py)
4. Nhấp vào nút **"Deploy"** để deploy code

![Create Function File](/images/12.png)

{{% notice download %}}
**📁 Source Code Required**: Copy nội dung từ link [storeapp-function.py](/downloads/storeapp-function.py) và paste vào file `function.py` trong Lambda editor.
{{% /notice %}}

### Bước 7: Configure Environment Variables

1. Chuyển sang tab **"Configuration"**
2. Trong sidebar, chọn **"Environment variables"**
3. Nhấp vào **"Edit"**

![Configure Environment Variables](/images/13.png)

### Bước 8: Add Firehose Stream Variable

1. Trong giao diện environment variables:
2. Nhấp **"Add environment variable"**
3. **Key**: `delivery_stream`
4. **Value**: `SI-Firehose` (tên Firehose stream đã tạo ở bước 3)
5. Nhấp **"Save"** để hoàn thành

![Add Environment Variable](/images/14.png)

{{% notice info %}}
**Environment Variables**: Cho phép Lambda function biết tên Firehose stream để gửi dữ liệu mà không cần hardcode trong source code.
{{% /notice %}}

## Xác minh

Sau khi hoàn thành các bước trên, Lambda function `StoreApp` của bạn đã được cấu hình với:

✅ **Runtime**: Python 3.13  
✅ **Handler**: function.lambda_handler  
✅ **Source Code**: Deployed successfully  
✅ **Environment Variable**: delivery_stream = SI-Firehose  

{{% notice success %}}
**Hoàn thành Phần 1!** StoreApp Lambda function đã được tạo và cấu hình thành công. Trong bước tiếp theo, chúng ta sẽ cấu hình permissions và test function.
{{% /notice %}}