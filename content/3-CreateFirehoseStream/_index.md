---
title : "Data Firehose Stream"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

In this module, you will create a Kinesis Data Firehose delivery stream - the core component of your streaming analytics pipeline. Firehose will collect inventory data from StoreApp and automatically write it to the S3 consumption bucket with optimized format for analytics.

## Kinesis Data Firehose Overview

Amazon Kinesis Data Firehose is a fully-managed service that helps you:

- **Automatically collect and transform** streaming data from multiple sources
- **Write data to data lake** with optimized format (Parquet) for analytics
- **Dynamic Partitioning** to optimize Athena query performance
- **Format conversion** from JSON to Parquet automatically
- **Retry and error handling** to ensure data reliability

### Architecture Integration

In our pipeline:
1. **StoreApp** → streams inventory data → **Firehose**
2. **Firehose** → converts JSON to Parquet → **S3 Bucket**
3. **Firehose** → updates metadata → **Glue Data Catalog** 
4. **Athena** → queries optimized data → **Analytics insights**

## Step-by-Step Instructions

### Step 1: Navigate to Kinesis Console

1. Go to AWS Console search bar
2. Search **"Kinesis"**
3. Click on **"Kinesis"**

![Navigate to Kinesis](/images/1.png)

### Step 2: Access Data Firehose

1. In the **"Get started"** interface, select **"Amazon Data Firehose"**
2. Click **"Create Firehose stream"** to start creating a firehose stream

![Access Data Firehose](/images/2.png)

### Step 3: Configure Source and Destination

1. **Source**: Select **"Direct PUT"**
2. **Destination**: Select **"Amazon S3"**
3. **Firehose stream name**: Name it `SI-Firehose`

![Configure Source and Destination](/images/3.png)

{{% notice info %}}
**Direct PUT**: Means applications will send data directly to the Firehose stream instead of through an intermediate Kinesis Data Stream.
{{% /notice %}}

### Step 4: Enable Record Format Conversion

1. Under **"Transform and convert records"** → **"Convert record format"**
2. Enable **"Enable record format conversion"**
3. After enabling, additional details will appear:
   - **AWS Glue Region**: Select the same region you're using (Singapore)
   - **AWS Glue Database**: Select `conversion_db`
   - **AWS Glue Table**: Select `conversion_table`

![Enable Record Format Conversion](/images/4.png)

{{% notice tip %}}
**Format Conversion**: Converting from JSON to Parquet reduces file size by up to 80% and significantly speeds up Athena queries.
{{% /notice %}}

### Step 5: Configure S3 Destination and Dynamic Partitioning

1. **Destination Settings** → **S3 bucket**: Select the consumption bucket created in section 2.1
2. **Dynamic partitioning**: Enable **"Enabled"**
3. **Inline parsing for JSON**: Enable **"Enabled"**

![Configure S3 and Dynamic Partitioning](/images/5.png)

### Step 6: Add Dynamic Partitioning Keys

1. In the **"Dynamic partitioning keys"** section, add the keys as shown in the image
2. After adding the keys, the **"S3 bucket prefix"** will be automatically filled
3. To ensure accuracy, copy and paste the following into **S3 bucket prefix**:
   ```
   store-data/store_id=!{partitionKeyFromQuery:store_id}/!{partitionKeyFromQuery:year}/!{partitionKeyFromQuery:month}/!{partitionKeyFromQuery:day}/!{partitionKeyFromQuery:hour}/
   ```
4. **S3 bucket error output prefix**: Enter `error`
5. **Retry duration**: Enter `60` seconds

![Add Dynamic Partitioning Keys](/images/6.png)

{{% notice info %}}
**Dynamic Partitioning**: Automatically organizes data by store_id and timestamp, helping Athena query faster by only scanning necessary partitions.
{{% /notice %}}

### Step 7: Configure IAM Role and Create Stream

1. Expand the **"Advanced settings"** section
2. **Service access**: Select **"Choose existing IAM role"**
3. Select the **"FirehoseWorkshop"** IAM role created in the previous step
4. Scroll down and click **"Create firehose stream"**

![Configure IAM and Create](/images/7.png)

### Step 8: Verification

After completing the setup, you should see the Firehose stream `SI-Firehose` successfully created with status **"Active"**.

![Firehose Stream Created](/images/8.png)

## Verification Checklist

Confirm the following configurations are set correctly:

✅ **Source**: Direct put  
✅ **Destination**: Amazon S3 (your consumption bucket)  
✅ **Format conversion**: Enabled (JSON → Parquet)  
✅ **Glue integration**: conversion_db.conversion_table  
✅ **Dynamic partitioning**: Enabled with appropriate keys  
✅ **IAM role**: FirehoseWorkshop  
✅ **Status**: Active  

{{% notice success %}}
**Complete!** Kinesis Data Firehose stream is now ready to receive streaming data from StoreApp and automatically write to the data lake with optimized format.
{{% /notice %}}

{{% notice warning %}}
**Cost Note**: Active Firehose stream will incur costs based on the amount of data processed. Remember to cleanup resources after completing the workshop.
{{% /notice %}}
