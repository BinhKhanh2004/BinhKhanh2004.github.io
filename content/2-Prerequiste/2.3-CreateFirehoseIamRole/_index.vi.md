---
title : "Create IAM Role for Kinesis Data Firehose"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

Trong bước này, bạn sẽ tạo một IAM Role cho phép Kinesis Data Firehose có quyền truy cập vào S3 bucket và AWS Glue Data Catalog để ghi dữ liệu streaming inventory.

## Tại sao cần IAM Role?

IAM Role cung cấp các quyền cần thiết cho Kinesis Data Firehose để:
- **Ghi dữ liệu vào S3**: Lưu trữ streaming data vào consumption bucket
- **Truy cập Glue Data Catalog**: Cập nhật table metadata và schema
- **Bảo mật**: Tuân thủ nguyên tắc "least privilege" của AWS

## Step-by-Step Instructions

### Step 1: Navigate to IAM Console

1. Từ trang chủ **AWS Management Console**, tìm thanh search ở phía trên
2. Gõ **"iam"** trong thanh tìm kiếm
3. Trong phần **"IAM Features"**, nhấp vào **"Roles"**

![Navigate to IAM Roles](/images/0_14.png)

### Step 2: Create New Role

1. Ở góc phía trên cùng bên phải của trang IAM Roles
2. Nhấp vào nút **"Create role"**

![Create Role Button](/images/0_15.png)

### Step 3: Configure Trusted Entity

1. **Trusted entity type**: Giữ mặc định **"AWS service"**
2. Trong phần **"Use case"**, tìm và chọn **"Firehose"** từ danh sách
3. Nhấp **"Next"**

![Configure Trusted Entity](/images/0_16.png)

### Step 4: Add Permissions

1. Chúng ta sẽ thêm vào 2 role chủ yếu dành cho 2 service:
2. Tìm kiếm và thêm **"AmazonS3FullAccess"**
3. Tìm kiếm và thêm **"AWSGlueServiceRole"** 
4. Nhấp **"Next"**

![Add Permissions](/images/0_17_1.png)

{{% notice warning %}}
**Lưu ý về Security**: Trong workshop này, chúng ta sử dụng **FullAccess** permissions để thuận tiện cho việc học tập. Tuy nhiên, trong môi trường production thực tế, bạn **KHÔNG BAO GIỜ** nên sử dụng FullAccess permissions. Thay vào đó, hãy áp dụng nguyên tắc **"Least Privilege"** - chỉ cấp những quyền tối thiểu cần thiết cho từng tác vụ cụ thể.
{{% /notice %}}

### Step 5: Name and Create Role

1. Chúng ta sẽ đặt tên role này là **"FirehoseWorkshop"**
2. Review phần **"Permissions"** đã có 2 service chính được add:
   - AmazonS3FullAccess
   - AWSGlueServiceRole
3. Nhấp **"Create role"**

![Create Role Final](/images/0_17.png)

## Verification

Sau khi tạo thành công, bạn sẽ thấy role `FirehoseWorkshop` trong danh sách với trusted entity `firehose.amazonaws.com` và 2 permissions đã được attach.

{{% notice success %}}
**Hoàn thành!** IAM Role cho Kinesis Data Firehose đã được tạo thành công và sẵn sàng sử dụng.
{{% /notice %}}

{{% notice tip %}}
**Lưu ý**: Ghi nhớ tên role `FirehoseWorkshop` để sử dụng trong bước cấu hình Firehose delivery stream tiếp theo.
{{% /notice %}}

Tiếp tục với: [**Create Kinesis Data Firehose Delivery Stream**](../2.4-create-firehose-stream/)