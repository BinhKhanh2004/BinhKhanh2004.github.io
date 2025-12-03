---
title : "Resource Cleanup"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

In this module, you will clean up all AWS resources created during the workshop to avoid unexpected costs. The cleanup will be performed in reverse order of creation to ensure no dependency errors.

## Why Resource Cleanup is Important

- **Cost Savings**: Services like Firehose, Lambda, and S3 storage continue to incur charges if not deleted
- **Resource Management**: Avoid cluttering your AWS account with unused resources
- **Security**: Remove buckets and functions to avoid unnecessary security risks

## Cleanup Order

1. **Amazon S3** - Delete consumption bucket
2. **Amazon SQS** - Delete notification queues  
3. **AWS Glue** - Delete database and tables
4. **AWS Lambda** - Delete functions

---

## Step 1: Clean Up Amazon S3 Bucket

### Step 1.1: Access S3 Console

1. Open AWS Console and search for **"S3"**
2. Click **"S3"** to access S3 console
3. Find and select the **consumption bucket** you created at the beginning of the workshop
4. Click **"Delete"**

![Navigate to S3 and Delete Bucket](/images/del_1.png)

### Step 1.2: Empty Bucket Before Deletion

1. In the **"Delete bucket"** interface, you'll see a message that the bucket must be emptied first
2. Click **"Empty bucket"** to delete all objects in the bucket

![Empty Bucket First](/images/del_2.png)

### Step 1.3: Confirm Empty Bucket

1. In the **"Empty bucket"** dialog, type **"permanently delete"** to confirm
2. Click **"Empty"** to execute the deletion of all objects

![Confirm Empty Bucket](/images/del_3.png)

{{% notice warning %}}
**Warning**: Emptying the bucket will permanently delete all data. Ensure you have backed up important data if needed.
{{% /notice %}}

### Step 1.4: Delete Bucket

1. After the bucket has been successfully emptied, return to the delete bucket interface
2. Type the **exact name of the S3 bucket** to confirm
3. Click **"Delete bucket"** to complete the deletion

![Confirm Delete Bucket](/images/del_4.png)

---

## Step 2: Clean Up Amazon SQS Queues

### Step 2.1: Access SQS Console

1. Open AWS Console and search for **"SQS"**
2. Click **"SQS"** to access SQS console
3. Select **each Queue** you created in the workshop
4. Click **"Delete"**

![Navigate to SQS and Delete Queues](/images/del_5.png)

### Step 2.2: Confirm Delete Queue

1. In the confirmation dialog, type **"delete"** to confirm
2. Click **"Delete"** to delete the queue
3. **Repeat** this process for all created queues

![Confirm Delete Queue](/images/del_6.png)

{{% notice info %}}
**Note**: You can select multiple queues at once for faster deletion by holding Ctrl and clicking on the queues.
{{% /notice %}}

---

## Step 3: Clean Up AWS Glue Database

### Step 3.1: Access Glue Console

1. Open AWS Console and search for **"Glue"**
2. Click **"AWS Glue"** to access Glue console
3. In the left sidebar, select **"Databases"**
4. Find and select **"conversion_db"**
5. Click **"Delete"**

![Navigate to Glue and Delete Database](/images/del_7.png)

### Step 3.2: Confirm Delete Database

1. In the confirmation dialog, read the message about deleting the database carefully
2. Click **"Delete"** to confirm database deletion

![Confirm Delete Glue Database](/images/del_8.png)

{{% notice tip %}}
**Information**: Deleting the database will automatically delete all tables within it, including the `conversion_table` we created.
{{% /notice %}}

---

## Step 4: Clean Up AWS Lambda Functions

### Step 4.1: Access Lambda Console

1. Open AWS Console and search for **"Lambda"**
2. Click **"Lambda"** to access Lambda console
3. **Select all** Lambda functions you created in the workshop
4. Click **"Actions"** → **"Delete"**

![Navigate to Lambda and Delete Functions](/images/del_9.png)

### Step 4.2: Confirm Delete Functions

1. In the confirmation dialog, carefully read the list of functions to be deleted
2. Type **"delete"** to confirm
3. Click **"Delete"** to complete the deletion

![Confirm Delete Lambda Functions](/images/del_10.png)

{{% notice warning %}}
**Warning**: Deleting Lambda functions is irreversible. Ensure you have backed up the source code if you need to use it again.
{{% /notice %}}

---

## Additional Resource Cleanup

### Kinesis Data Firehose

If the Firehose stream is still running:

1. Access **Kinesis Console**
2. Select **"Data Firehose"**
3. Select **"SI-Firehose"** stream
4. Click **"Delete"** and confirm

### IAM Roles (Optional)

For complete cleanup:

1. Access **IAM Console**
2. Select **"Roles"**  
3. Find all the roles we created
4. Delete roles if not needed for other purposes

---

## Verification Checklist

Verify that all resources have been successfully deleted:

✅ **S3 Bucket**: Consumption bucket has been deleted  
✅ **SQS Queues**: All notification queues have been deleted  
✅ **Glue Database**: conversion_db and conversion_table have been deleted  
✅ **Lambda Functions**: All functions have been deleted  
✅ **Firehose Stream**: SI-Firehose stream has been deleted (if applicable)  
✅ **IAM Roles**: FirehoseWorkshop role has been deleted (optional)  

{{% notice success %}}
**Complete!** All AWS workshop resources have been successfully cleaned up. You will not be charged for these resources anymore.
{{% /notice %}}

{{% notice info %}}
**Final Note**: It may take a few minutes for AWS to complete the deletion of all resources. You can check the billing dashboard after 24 hours to ensure no charges are incurred.
{{% /notice %}}