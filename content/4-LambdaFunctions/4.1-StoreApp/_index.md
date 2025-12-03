---
title : "Create StoreApp Function"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

In this step, you will create the **StoreApp Lambda function** - an application that simulates stores sending real-time inventory data to the Kinesis Data Firehose stream. This Lambda function will generate and stream store inventory data to serve the analytics pipeline.

## StoreApp Lambda Function Overview

The StoreApp Lambda function plays a crucial role in the streaming analytics architecture:

- **Data Generator**: Creates simulated inventory data from multiple different stores
- **Streaming Integration**: Sends data directly to Kinesis Data Firehose
- **Event-Driven**: Can be triggered manually or on a schedule
- **JSON Format**: Generates data with JSON structure compatible with Glue table schema

## Step-by-Step Instructions

### Step 1: Navigate to Lambda Console

1. In the AWS Console search bar
2. Type **"lambda"**
3. Select **"Lambda"** from the search results

![Navigate to Lambda](/images/9.png)

### Step 2: Create New Function

1. Click the **"Create function"** button in the top right corner

![Create Function](/images/10.png)

### Step 3: Configure Function Settings

1. **Function name**: Name it `StoreApp`
2. **Runtime**: Select **"Python 3.13"**
3. Leave other settings as default
4. Click **"Create function"** to proceed to the next step

![Configure Function Settings](/images/11.png)

{{% notice info %}}
**Python 3.13**: Latest version with improved performance and better support for AWS SDK (boto3).
{{% /notice %}}

### Step 4: Edit Runtime Settings

1. After creating the function, in the **"Code"** section
2. Scroll down to **"Runtime settings"**
3. Click **"Edit"**

![Edit Runtime Settings](/images/12_1.png)

### Step 5: Update Handler Configuration

1. In the new interface that appears:
   - **Runtime**: Select **"Python 3.13"**
   - **Handler**: Enter `function.lambda_handler`
2. Click **"Save"** to save the configuration

![Update Handler](/images/12_2.png)

{{% notice tip %}}
**Handler**: `function.lambda_handler` means Lambda will call the `lambda_handler()` function in the `function.py` file.
{{% /notice %}}

### Step 6: Create Function Code File

1. In the **"Code"** section, find and click the new file creation icon (highlighted in the image)
2. Name the new file: `function.py`
3. Copy content from the following link and paste into the file: [📁 storeapp-function.py](/downloads/storeapp-function.py)
4. Click the **"Deploy"** button to deploy the code

![Create Function File](/images/12.png)

{{% notice download %}}
**📁 Source Code Required**: Copy content from the link [storeapp-function.py](/downloads/storeapp-function.py) and paste into the `function.py` file in the Lambda editor.
{{% /notice %}}

### Step 7: Configure Environment Variables

1. Switch to the **"Configuration"** tab
2. In the sidebar, select **"Environment variables"**
3. Click **"Edit"**

![Configure Environment Variables](/images/13.png)

### Step 8: Add Firehose Stream Variable

1. In the environment variables interface:
2. Click **"Add environment variable"**
3. **Key**: `delivery_stream`
4. **Value**: `SI-Firehose` (name of the Firehose stream created in step 3)
5. Click **"Save"** to complete

![Add Environment Variable](/images/14.png)

{{% notice info %}}
**Environment Variables**: Allows the Lambda function to know the Firehose stream name for sending data without hardcoding it in the source code.
{{% /notice %}}

## Verification

After completing the above steps, your `StoreApp` Lambda function has been configured with:

✅ **Runtime**: Python 3.13  
✅ **Handler**: function.lambda_handler  
✅ **Source Code**: Deployed successfully  
✅ **Environment Variable**: delivery_stream = SI-Firehose  

{{% notice success %}}
**Part 1 Complete!** StoreApp Lambda function has been successfully created and configured. In the next step, we'll configure permissions and test the function.
{{% /notice %}}