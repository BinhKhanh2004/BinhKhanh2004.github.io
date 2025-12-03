---
title : "Cấu hình và test StoreApp"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

Trong bước này, bạn sẽ cấu hình IAM permissions cho StoreApp Lambda function để có thể gửi dữ liệu vào Kinesis Data Firehose, sau đó test function để xác minh dữ liệu được stream thành công vào S3 bucket.

## Tại sao phải cấu hình Permissions?

Lambda function cần những quyền cụ thể để:

- **Access Kinesis Data Firehose**: Gửi inventory records vào SI-Firehose stream
- **Write to CloudWatch Logs**: Log execution details để troubleshooting
- **Security Best Practice**: Tuân thủ nguyên tắc least privilege

### Permission Model
AWS Lambda tự động tạo execution role khi tạo function, nhưng chúng ta cần thêm Firehose permissions để function có thể stream dữ liệu.

## Hướng dẫn từng bước

### Bước 1: Create Test Event

1. Quay trở lại Lambda function **"StoreApp"**
2. Bấm vào tab **"Test"** ở phía trên
3. Chọn **"Create new event"**
4. **Event name**: Đặt tên `test`
5. Giữ template mặc định
6. Bấm **"Save"** để hoàn thành

![Create Test Event](/images/15.png)

{{% notice info %}}
**Test Event**: Cho phép bạn manually trigger Lambda function để test functionality trước khi integrate với các services khác.
{{% /notice %}}

### Bước 2: Navigate to IAM Roles

1. Để Lambda có thể hoạt động, cần thêm quyền cho IAM role
2. Mở tab mới, vào **IAM Console**
3. Vào phần **"Roles"**
4. Search **"store"** để hiển thị role IAM của lambda "StoreApp"
5. Chọn role đó (thường có tên dạng `StoreApp-role-xxxxx`)

![Navigate to IAM Roles](/images/15_1.png)

### Bước 3: Add Firehose Permissions

1. Trong IAM role page, tìm phần **"Add permissions"**
2. Chọn **"Attach policies"**

![Add Permissions](/images/15_2.png)

### Bước 4: Attach Firehose Policy

1. Trong thanh tìm kiếm permissions, nhập **"firehose"**
2. Tìm và check **"AmazonKinesisFirehoseFullAccess"** 
3. Bấm **"Add permissions"** để attach policy

![Attach Firehose Policy](/images/15_3.png)

{{% notice warning %}}
**Security Note**: Trong production, nên sử dụng custom policy với permissions tối thiểu thay vì FullAccess. Workshop này dùng FullAccess để đơn giản hóa.
{{% /notice %}}

### Bước 5: Test Lambda Function

1. Quay trở lại Lambda **"StoreApp"**
2. Vào tab **"Test"** 
3. Bấm nút **"Test"** để thực hiện test event

![Test Lambda Function](/images/16.png)

### Bước 6: Review Test Results

1. Sau khi thực hiện test event thành công
2. Bản log chi tiết sẽ hiển thị execution results
3. Kiểm tra status **"Succeeded"** và review logs để đảm bảo dữ liệu đã được gửi

![Review Test Results](/images/17.png)

{{% notice success %}}
**Test Successful**: Nếu thấy status "Succeeded" và không có error logs, Lambda function đã gửi dữ liệu thành công vào Firehose.
{{% /notice %}}

### Bước 7: Verify Data in S3 - Access Bucket

1. Mở tab mới, truy cập vào **S3 Console**
2. Vào **consumption-bucket** đã tạo từ đầu workshop

![Access S3 Bucket](/images/18.png)

### Bước 8: Navigate to Bucket Contents

1. Click vào consumption bucket để xem contents

![Navigate Bucket Contents](/images/19.png)

### Bước 9: Refresh and Check Objects

1. **Refresh** lại trang để cập nhật objects mới nhất
2. Bạn sẽ thấy thư mục **store-data** đã được tạo bởi Firehose

![Refresh and Check Objects](/images/20.png)

{{% notice tip %}}
**Dynamic Partitioning**: Firehose tự động tạo folder structure theo pattern đã cấu hình: `store-data/store_id=XXX/year/month/day/hour/`
{{% /notice %}}

### Bước 10: Verify Firehose Output Files

1. Điều hướng tới đường dẫn partitioned folders
2. Bạn sẽ thấy file output của SI-Firehose (format Parquet)
3. Đây chính là dữ liệu inventory đã được convert và store trong data lake

![Verify Firehose Output](/images/21.png)

## Verification Checklist

Xác nhận các điều kiện sau đã hoàn thành:

✅ **IAM Permissions**: StoreApp role có AmazonKinesisFirehoseFullAccess  
✅ **Test Event**: Created và executed successfully  
✅ **Lambda Logs**: Status "Succeeded" không có errors  
✅ **S3 Data**: Files xuất hiện trong consumption bucket  
✅ **Data Structure**: Folders được tạo theo dynamic partitioning pattern  
✅ **File Format**: Parquet files generated bởi Firehose  

{{% notice success %}}
**End-to-End Test Successful!** Dữ liệu inventory đã được stream thành công từ StoreApp → Firehose → S3. Pipeline cơ bản đã hoạt động!
{{% /notice %}}

{{% notice info %}}
**What Happened**: StoreApp generated inventory data → sent to SI-Firehose → converted to Parquet → stored in S3 với dynamic partitioning → ready for Athena analytics!
{{% /notice %}}