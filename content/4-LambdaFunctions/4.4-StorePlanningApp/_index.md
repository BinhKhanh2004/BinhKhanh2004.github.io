---
title : "StorePlanningApp  Function"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---

In this step, you will create the **StorePlanningApp Lambda Function** - an application that processes planning logic for the store system. This function will receive messages from the SQS Queue, perform data analysis from Athena, and generate supply planning strategies.

## StorePlanningApp Lambda Function Overview

StorePlanningApp plays a crucial role in the analytics architecture:

- **Message Consumer**: Receives and processes messages from SQS Store_Queue
- **Data Analytics**: Queries data from Athena/Glue for inventory analysis
- **Planning Logic**: Calculates demand and creates supply plans
- **Result Storage**: Stores analysis results in S3 bucket

## Step-by-Step Instructions

### Step 1: Navigate to Lambda Console

1. In the AWS Console search bar
2. Type **"lambda"**
3. Select **"Lambda"** from the search results

![Navigate to Lambda](/images/22.png)

### Step 2: Create New Function

1. Click the **"Create function"** button
2. **Function name**: Name it `StorePlanningApp`
3. **Runtime**: Select **"Python 3.13"**
4. Leave other configurations as default
5. Click **"Create function"**

![Create Planning Lambda](/images/23.png)

{{% notice info %}}
**StorePlanningApp**: This function will contain more complex logic than StoreApp, including Athena queries and planning algorithms.
{{% /notice %}}

### Step 3: Deploy Function Code

1. In the Lambda code interface of "StorePlanningApp"
2. Perform the same steps as done with "StoreApp":
   - Create `function.py` file
   - Configure handler to `function.lambda_handler`
3. Copy and paste code from this link: [📁 planning-function.py](/downloads/planning-function.py)
4. Click **"Deploy"** to deploy the code

![Deploy Planning Code](/images/24.png)

{{% notice download %}}
**📁 Source Code Required**: Copy content from link [planning-function.py](/downloads/planning-function.py) and paste into the `function.py` file in the Lambda editor.
{{% /notice %}}

### Step 4: Configure Environment Variables

1. Navigate to **"Configuration"** section
2. Select **"Environment variables"** 
3. Click **"Edit"**

Add the following 4 environment variables:

| Key | Value | Description |
|-----|--------|-------------|
| `glue_db` | `conversion_db` | Glue database name |
| `glue_table` | `conversion_table` | Glue table name |
| `output_bucket` | `s3://consumption-bucket-yourname/` | S3 bucket output |
| `queue_url` | `https://sqs.ap-southeast-1.amazonaws.com/yourID/Store_Queue` | SQS Queue URL |

![Configure Environment Variables](/images/26.png)

{{% notice warning %}}
**Replace Information**: 
- Replace `yourname` in bucket name with your name
- Replace `yourID` in queue URL with your AWS Account ID
{{% /notice %}}

### Step 5: Configure Timeout

1. Still in the **"Configuration"** section
2. Select **"General configuration"**
3. Click **"Edit"**

![Navigate General Config](/images/27.png)

4. Set **Timeout** to **"2 min"** (120 seconds)
5. Click **"Save"** to save configuration

![Set Timeout](/images/28.png)

{{% notice tip %}}
**Why 2 minutes timeout?**: StorePlanningApp needs time to query Athena and process data, longer timeout ensures function doesn't terminate early.
{{% /notice %}}

### Step 6: Configure IAM Permissions

1. Navigate to **IAM Console**
2. In the search bar, type **"store"** 
3. Find and select role **"StorePlanningApp-role-xxxxx"**

![Find Planning Role](/images/21_5.png)

4. Click **"Add permissions"** → **"Attach policies"**

![Add Permissions](/images/21_6.png)

5. Add the following policies (search and attach each policy):
   - ✅ **AmazonAthenaFullAccess** 
   - ✅ **AmazonS3FullAccess**
   - ✅ **AmazonSQSFullAccess** 
   - ✅ **AWSGlueConsoleFullAccess**

![Attach Policies](/images/21_7.png)

{{% notice info %}}
**IAM Permissions Explained**:
- **Athena**: Query data from data lake
- **S3**: Read/write result files
- **SQS**: Receive messages from queue
- **Glue**: Access metadata catalog
{{% /notice %}}

### Step 7: Test Lambda Function

1. Return to Lambda **"StorePlanningApp"**
2. Navigate to **"Test"** section
3. Create test event named **"test"**
4. Click **"Test"** button to execute

![Create Test Event](/images/29.png)

### Step 8: Verify Test Results

After successful test, you should see:

- ✅ **Execution result**: succeeded
- ✅ **Function logs**: Detailed processing information
- ✅ **Duration**: Execution time
- ✅ **Memory used**: Resource consumption

![Test Results](/images/30.png)

## Verify Function Operation

After completing the above steps, StorePlanningApp Lambda function has:

✅ **Runtime**: Python 3.13  
✅ **Handler**: function.lambda_handler  
✅ **Source Code**: Planning logic deployed  
✅ **Environment Variables**: 4 variables configured  
✅ **Timeout**: 2 minutes  
✅ **IAM Permissions**: 4 policies attached  
✅ **Test Status**: Successfully executed  

{{% notice success %}}
**StorePlanningApp Complete!** Lambda function has been created, configured, and tested successfully. Function is ready to process planning logic from SQS messages.
{{% /notice %}}

## Summary

StorePlanningApp Lambda function now:

- **Receives and processes** messages from SQS Queue
- **Queries data** from Athena for analytics  
- **Executes planning logic** based on inventory data
- **Stores results** in S3 bucket
- **Ready to scale** with message volume

This function is the core component in our store planning and analytics pipeline!