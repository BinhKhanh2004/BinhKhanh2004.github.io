---
title : "Tạo S3 Bucket"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

Trong bước này, bạn sẽ tạo một S3 bucket để phục vụ như **vùng tiêu thụ** cho dữ liệu hàng tồn kho streaming của bạn. Bucket này sẽ hoạt động như một data lake nơi tất cả các bản ghi hàng tồn kho từ các cửa hàng của bạn sẽ được lưu trữ và cung cấp để phân tích.

## Tại sao chúng ta cần Bucket này?

S3 consumption bucket phục vụ nhiều mục đích trong pipeline streaming analytics của chúng ta:

- **Lưu trữ Data Lake**: Kho lưu trữ tập trung cho tất cả dữ liệu hàng tồn kho streaming
- **Nguồn dữ liệu Athena**: Amazon Athena sẽ truy vấn dữ liệu được lưu trữ trong bucket này
- **Đích đến Firehose**: Kinesis Data Firehose sẽ giao các bản ghi streaming đến đây
- **Lưu trữ hiệu quả về chi phí**: S3 cung cấp lưu trữ bền vững, có thể mở rộng với chi phí thấp

## Hướng dẫn từng bước

### Bước 1: Điều hướng đến S3 Console

1. Từ trang chủ **AWS Management Console**, tìm thanh tìm kiếm ở phía trên
2. Gõ **"s3"** trong trường tìm kiếm
3. Nhấp vào **Amazon S3** từ kết quả tìm kiếm

![Navigate to S3](/images/0_1.png)

### Bước 2: Truy cập tạo Bucket

1. Nhấp vào nút **"Create bucket"** để bắt đầu quá trình tạo bucket

![S3 Buckets Dashboard](/images/0_2.png)

### Bước 3: Cấu hình cài đặt Bucket

1. Trong trường **Bucket name**, nhập: `consumption-bucket-yourname`
   
   {{% notice warning %}}
   **Quan trọng**: Thay thế "yourname" bằng tên thật của bạn hoặc một định danh duy nhất (ví dụ: `consumption-bucket-nguyenvana`). Tên S3 bucket phải **duy nhất toàn cầu** trên tất cả các tài khoản AWS trên toàn thế giới.
   {{% /notice %}}

2. **Region**: Đảm bảo bạn đang tạo bucket trong **Singapore / ap-southeast-1**
3. Để tất cả các cài đặt khác ở mặc định (chúng ta sẽ sử dụng các cài đặt bảo mật được khuyến nghị)
4. Cuộn xuống cuối trang
5. Nhấp **"Create bucket"** để hoàn thành việc tạo

![Create S3 Bucket Configuration](/images/0_3.png)

## Xác minh

Sau khi tạo thành công, bạn sẽ thấy bucket mới của mình được liệt kê trong S3 console với tên `consumption-bucket-yourname`.

{{% notice tip %}}
**Mẹo hữu ích**: Ghi chú lại tên chính xác của bucket. Bạn sẽ cần điều này khi cấu hình Kinesis Data Firehose trong các module tiếp theo.
{{% /notice %}}

{{% notice info %}}
**Quy tắc đặt tên Bucket**: Tên S3 bucket phải dài 3-63 ký tự, chỉ chứa chữ cái thường, số và dấu gạch ngang, và không thể bắt đầu hoặc kết thúc bằng dấu gạch ngang.
{{% /notice %}}