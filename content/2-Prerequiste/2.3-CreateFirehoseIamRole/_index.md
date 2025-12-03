---
title : "Create IAM Role for Kinesis Data Firehose"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

In this step, you will create an IAM Role that allows Kinesis Data Firehose to access your S3 bucket and AWS Glue Data Catalog for writing streaming inventory data.

## Why Do We Need an IAM Role?

The IAM Role provides necessary permissions for Kinesis Data Firehose to:
- **Write data to S3**: Store streaming data in the consumption bucket
- **Access Glue Data Catalog**: Update table metadata and schema
- **Security**: Follow AWS "least privilege" security best practices

## Step-by-Step Instructions

### Step 1: Navigate to IAM Console

1. From the **AWS Management Console** home page, locate the search bar at the top
2. Type **"iam"** in the search field
3. Under **"IAM Features"**, click on **"Roles"**

![Navigate to IAM Roles](/images/0_14.png)

### Step 2: Create New Role

1. In the top-right corner of the IAM Roles page
2. Click the **"Create role"** button

![Create Role Button](/images/0_15.png)

### Step 3: Configure Trusted Entity

1. **Trusted entity type**: Keep the default **"AWS service"**
2. Under **"Use case"**, find and select **"Firehose"** from the list
3. Click **"Next"**

![Configure Trusted Entity](/images/0_16.png)

### Step 4: Add Permissions

1. We will add 2 main roles for 2 services:
2. Search and add **"AmazonS3FullAccess"**
3. Search and add **"AWSGlueServiceRole"**
4. Click **"Next"**

![Add Permissions](/images/0_17_1.png)

{{% notice warning %}}
**Security Note**: In this workshop, we use **FullAccess** permissions for learning convenience. However, in real-world production environments, you should **NEVER** use FullAccess permissions. Instead, apply the **"Least Privilege"** principle - only grant the minimum permissions necessary for each specific task.
{{% /notice %}}

### Step 5: Name and Create Role

1. We will name this role **"FirehoseWorkshop"**
2. Review the **"Permissions"** section has 2 main services added:
   - AmazonS3FullAccess
   - AWSGlueServiceRole
3. Click **"Create role"**

![Create Role Final](/images/0_17.png)

## Verification

After successful creation, you should see the `FirehoseWorkshop` role in the list with trusted entity `firehose.amazonaws.com` and 2 permissions attached.

{{% notice success %}}
**Complete!** IAM Role for Kinesis Data Firehose has been successfully created and is ready to use.
{{% /notice %}}
