---
title : "Dọn dẹp tài nguyên"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

Trong module này, bạn sẽ dọn dẹp tất cả các tài nguyên AWS đã tạo trong workshop để tránh phát sinh chi phí không mong muốn. Việc dọn dẹp sẽ được thực hiện theo thứ tự ngược lại với quá trình tạo để đảm bảo không có lỗi dependency.

## Tại sao cần dọn dẹp tài nguyên?

- **Tiết kiệm chi phí**: Các dịch vụ như Firehose, Lambda và S3 storage sẽ tiếp tục tính phí nếu không xóa
- **Quản lý tài nguyên**: Tránh tình trạng tài khoản AWS bị cluttered với các resource không sử dụng
- **Bảo mật**: Xóa các bucket và function để tránh rủi ro bảo mật không cần thiết

## Thứ tự dọn dẹp

1. **Amazon S3** - Xóa consumption bucket
2. **Amazon SQS** - Xóa notification queues  
3. **AWS Glue** - Xóa database và tables
4. **AWS Lambda** - Xóa các functions

---

## Bước 1: Dọn dẹp Amazon S3 Bucket

### Bước 1.1: Truy cập S3 Console

1. Mở AWS Console và tìm kiếm **"S3"**
2. Nhấp vào **"S3"** để truy cập S3 console
3. Tìm và chọn **consumption bucket** mà bạn đã tạo từ đầu workshop
4. Nhấp vào **"Delete"**

![Navigate to S3 and Delete Bucket](/images/del_1.png)

### Bước 1.2: Empty Bucket trước khi Delete

1. Trong giao diện **"Delete bucket"**, bạn sẽ thấy thông báo rằng bucket phải được empty trước
2. Nhấp vào **"Empty bucket"** để xóa tất cả objects trong bucket

![Empty Bucket First](/images/del_2.png)

### Bước 1.3: Xác nhận Empty Bucket

1. Trong dialog **"Empty bucket"**, gõ **"permanently delete"** để xác nhận
2. Nhấp **"Empty"** để thực hiện việc xóa tất cả objects

![Confirm Empty Bucket](/images/del_3.png)

{{% notice warning %}}
**Cảnh báo**: Việc empty bucket sẽ xóa vĩnh viễn tất cả dữ liệu. Đảm bảo bạn đã backup dữ liệu quan trọng nếu cần.
{{% /notice %}}

### Bước 1.4: Delete Bucket

1. Sau khi bucket đã được empty thành công, quay lại giao diện delete bucket
2. Gõ **tên chính xác của S3 bucket** để xác nhận
3. Nhấp **"Delete bucket"** để hoàn tất việc xóa

![Confirm Delete Bucket](/images/del_4.png)

---

## Bước 2: Dọn dẹp Amazon SQS Queues

### Bước 2.1: Truy cập SQS Console

1. Mở AWS Console và tìm kiếm **"SQS"**
2. Nhấp vào **"SQS"** để truy cập SQS console
3. Chọn **từng Queue** mà bạn đã tạo trong workshop
4. Nhấp vào **"Delete"**

![Navigate to SQS and Delete Queues](/images/del_5.png)

### Bước 2.2: Xác nhận Delete Queue

1. Trong dialog xác nhận, gõ **"delete"** để confirm
2. Nhấp **"Delete"** để xóa queue
3. **Lặp lại** quá trình này cho tất cả queues đã tạo

![Confirm Delete Queue](/images/del_6.png)

{{% notice info %}}
**Lưu ý**: Bạn có thể select multiple queues cùng lúc để xóa nhanh hơn bằng cách giữ Ctrl và click vào các queues.
{{% /notice %}}

---

## Bước 3: Dọn dẹp AWS Glue Database

### Bước 3.1: Truy cập Glue Console

1. Mở AWS Console và tìm kiếm **"Glue"**
2. Nhấp vào **"AWS Glue"** để truy cập Glue console
3. Trong thanh sidebar bên trái, chọn **"Databases"**
4. Tìm và chọn **"conversion_db"**
5. Nhấp **"Delete"**

![Navigate to Glue and Delete Database](/images/del_7.png)

### Bước 3.2: Xác nhận Delete Database

1. Trong dialog xác nhận, đọc kỹ thông báo về việc xóa database
2. Nhấp **"Delete"** để xác nhận xóa database

![Confirm Delete Glue Database](/images/del_8.png)

{{% notice tip %}}
**Thông tin**: Việc xóa database sẽ tự động xóa tất cả các tables có trong database đó, bao gồm cả `conversion_table` mà chúng ta đã tạo.
{{% /notice %}}

---

## Bước 4: Dọn dẹp AWS Lambda Functions

### Bước 4.1: Truy cập Lambda Console

1. Mở AWS Console và tìm kiếm **"Lambda"**
2. Nhấp vào **"Lambda"** để truy cập Lambda console
3. **Chọn tất cả** các Lambda functions mà bạn đã tạo trong workshop
4. Nhấp **"Actions"** → **"Delete"**

![Navigate to Lambda and Delete Functions](/images/del_9.png)

### Bước 4.2: Xác nhận Delete Functions

1. Trong dialog xác nhận, đọc kỹ danh sách các functions sẽ bị xóa
2. Gõ **"delete"** để xác nhận
3. Nhấp **"Delete"** để hoàn tất việc xóa

![Confirm Delete Lambda Functions](/images/del_10.png)

{{% notice warning %}}
**Cảnh báo**: Việc xóa Lambda functions sẽ không thể hoàn tác. Đảm bảo bạn đã backup source code nếu cần sử dụng lại.
{{% /notice %}}

---

## Dọn dẹp các tài nguyên bổ sung

### Kinesis Data Firehose

Nếu Firehose stream vẫn đang chạy:

1. Truy cập **Kinesis Console**
2. Chọn **"Data Firehose"**
3. Select **"SI-Firehose"** stream
4. Nhấp **"Delete"** và xác nhận

### IAM Roles (Tùy chọn)

Nếu muốn dọn dẹp hoàn toàn:

1. Truy cập **IAM Console**
2. Chọn **"Roles"**  
3. Tìm các role chúng ta đã tạo
4. Xóa hết role nếu không cần sử dụng cho mục đích khác

---

## Verification Checklist

Kiểm tra các tài nguyên đã được xóa thành công:

✅ **S3 Bucket**: Consumption bucket đã bị xóa  
✅ **SQS Queues**: Tất cả notification queues đã bị xóa  
✅ **Glue Database**: conversion_db và conversion_table đã bị xóa  
✅ **Lambda Functions**: Tất cả functions đã bị xóa  
✅ **Firehose Stream**: SI-Firehose stream đã bị xóa (nếu có)  
✅ **IAM Roles**: FirehoseWorkshop role đã bị xóa (tùy chọn)  

{{% notice success %}}
**Hoàn tất!** Tất cả tài nguyên AWS của workshop đã được dọn dẹp thành công. Bạn sẽ không bị tính phí thêm cho các tài nguyên này.
{{% /notice %}}

{{% notice info %}}
**Lưu ý cuối**: Có thể mất vài phút để AWS hoàn tất việc xóa tất cả tài nguyên. Bạn có thể kiểm tra lại billing dashboard sau 24 giờ để đảm bảo không có charges nào phát sinh.
{{% /notice %}}