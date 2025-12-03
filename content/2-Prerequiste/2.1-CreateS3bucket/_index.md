---
title : "Create S3 Bucket"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

In this step, you will create an S3 bucket that will serve as the **consumption zone** for your streaming inventory data. This bucket will act as a data lake where all inventory records from your stores will be stored and made available for analytics.

## Why Do We Need This Bucket?

The S3 consumption bucket serves multiple purposes in our streaming analytics pipeline:

- **Data Lake Storage**: Centralized repository for all streaming inventory data
- **Athena Data Source**: Amazon Athena will query data stored in this bucket
- **Firehose Destination**: Kinesis Data Firehose will deliver streaming records here
- **Cost-Effective Storage**: S3 provides durable, scalable storage at low cost

## Step-by-Step Instructions

### Step 1: Navigate to S3 Console

1. From the **AWS Management Console** home page, locate the search bar at the top
2. Type **"s3"** in the search field
3. Click on **Amazon S3** from the search results

![Navigate to S3](/images/0_1.png)

### Step 2: Access Bucket Creation

1. Click the **"Create bucket"** button to start the bucket creation process

![S3 Buckets Dashboard](/images/0_2.png)

### Step 3: Configure Bucket Settings

1. In the **Bucket name** field, enter: `consumption-bucket-yourname`
   
   {{% notice warning %}}
   **Important**: Replace "yourname" with your actual name or a unique identifier (e.g., `consumption-bucket-nguyenvana`). S3 bucket names must be **globally unique** across all AWS accounts worldwide.
   {{% /notice %}}

2. **Region**: Ensure you're creating the bucket in **Singapore / ap-southeast-1**
3. Leave all other settings as default (we'll use the recommended security settings)
4. Scroll down to the bottom of the page
5. Click **"Create bucket"** to complete the creation

![Create S3 Bucket Configuration](/images/0_3.png)

## Verification

After successful creation, you should see your new bucket listed in the S3 console with the name `consumption-bucket-yourname`.

{{% notice tip %}}
**Pro Tip**: Take note of your exact bucket name. You'll need this when configuring Kinesis Data Firehose in the next modules.
{{% /notice %}}

{{% notice info %}}
**Bucket Naming Rules**: S3 bucket names must be 3-63 characters long, contain only lowercase letters, numbers, and hyphens, and cannot start or end with a hyphen.
{{% /notice %}}