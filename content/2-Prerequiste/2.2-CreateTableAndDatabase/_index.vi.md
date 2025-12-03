---
title : "Tạo Database & Table"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

Trong bước này, bạn sẽ tạo AWS Glue database và table sẽ phục vụ như metadata catalog cho dữ liệu hàng tồn kho streaming của bạn. Catalog này cho phép Amazon Athena hiểu và truy vấn dữ liệu được lưu trữ trong S3 consumption bucket của bạn.

## Tổng quan

AWS Glue Data Catalog hoạt động như kho metadata tập trung lưu trữ thông tin về cấu trúc, định dạng và vị trí dữ liệu của bạn. Khi bạn tạo database và table trong Glue, bạn về cơ bản đang tạo một schema mà Athena có thể sử dụng để diễn giải các file dữ liệu thô của bạn.

**Những gì chúng ta sẽ tạo:**
- **Database**: `conversion_db` - Container logic cho các table hàng tồn kho của chúng ta
- **Table**: `conversion_table` - Định nghĩa schema cho cấu trúc dữ liệu hàng tồn kho

## Phần A: Tạo Glue Database

### Bước 1: Điều hướng đến AWS Glue Console

1. Từ trang chủ **AWS Management Console**, tìm thanh tìm kiếm ở phía trên
2. Gõ **"Glue"** trong trường tìm kiếm
3. Nhấp vào **"AWS Glue"** từ kết quả tìm kiếm

![Navigate to AWS Glue](/images/0_4.png)

### Bước 2: Truy cập phần Databases

1. Trong AWS Glue console, nhìn vào panel điều hướng bên trái
2. Tìm và nhấp vào **"Databases"** dưới phần Data Catalog
3. Trong trang Databases, nhấp nút **"Add database"** ở góc trên bên phải

![AWS Glue Navigation](/images/0_5.png)

### Bước 3: Tạo Database

1. Trong trường **Database name**, nhập: `conversion_db`
2. Để các cài đặt khác ở mặc định
3. Nhấp **"Create database"** để hoàn thành việc tạo

![Create Glue Database](/images/0_6.png)

{{% notice success %}}
**Thành công!** Bạn đã tạo thành công database `conversion_db`. Database này sẽ phục vụ như container logic cho các table dữ liệu hàng tồn kho của chúng ta.
{{% /notice %}}

## Phần B: Tạo Glue Table

### Bước 4: Điều hướng đến phần Tables

1. Trong panel điều hướng bên trái, dưới **"Databases"**, nhấp vào **"Tables"**
2. Nhấp nút **"Add table"** ở góc trên bên phải

![Navigate to Tables](/images/0_7.png)

### Bước 5: Cấu hình Thông tin Cơ bản Table

1. **Table name**: Nhập `conversion_table`
2. **Database**: Chọn `conversion_db` từ dropdown (database chúng ta vừa tạo)
3. Để các cài đặt cơ bản khác ở mặc định

![Configure Table](/images/0_8.png)

### Bước 6: Cấu hình Data Store

1. Cuộn xuống phần **"Include path"**
2. Nhấp **"Browse S3"** hoặc nhập thủ công đường dẫn đến S3 bucket của bạn:
   ```
   s3://consumption-bucket-yourname/
   ```
   {{% notice info %}}
   Thay thế "yourname" bằng tên thật bạn đã sử dụng khi tạo S3 bucket ở bước 2.1
   {{% /notice %}}

3. Trong phần **"Data format"**, chọn **"Parquet"**
4. Nhấp **"Next"** để tiếp tục

![Configure Table Data Store](/images/0_9.png)

### Bước 7: Định nghĩa Schema sử dụng JSON

1. Ở trang định nghĩa schema, chọn **Edit schema as JSON**
2. Sao chép nội dung schema từ link này: [🔗 inventory-schema.json](/downloads/inventory-schema.json)
3. Dán nội dung JSON đã sao chép vào trường **Edit schema as JSON**
4. Nhấp **"Save"** để áp dụng schema

![Edit Schema as JSON](/images/0_10.png)
![Finalize Table Creation](/images/0_11.png)

{{% notice warning %}}
Cần Nội dung Schema: Bạn phải sao chép chính xác JSON schema từ link được cung cấp ở trên. Schema được định nghĩa trước này phù hợp với cấu trúc dữ liệu hàng tồn kho sẽ được stream từ StoreApp của bạn. Không được sửa đổi nội dung schema vì nó cần phù hợp với định dạng dữ liệu đến.
{{% /notice %}}

### Bước 8: Hoàn thành Tạo Table

1. Xem lại cấu hình table của bạn
2. Nhấp **"Next"** để tiếp tục đến bước cuối
3. Xem lại tóm tắt và nhấp **"Create table"** để hoàn thành

![Glue Database and Table Created](/images/0_12.png)

## Xác minh

Sau khi tạo thành công, bạn sẽ thấy:
- Database: `conversion_db` trong danh sách Databases
- Table: `conversion_table` dưới database `conversion_db`

![Review Table](/images/0_13.png)

{{% notice success %}}
**Chúc mừng!** Bạn đã tạo thành công cả Glue database và table. Amazon Athena giờ có thể sử dụng metadata catalog này để truy vấn dữ liệu hàng tồn kho streaming của bạn.
{{% /notice %}}