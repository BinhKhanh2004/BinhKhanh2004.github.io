---
title : "Create StoreTruckApp and Complete Pipeline"
date : "`r Sys.Date()`"
weight : 5
chapter : false
pre : " <b> 4.5 </b> "
---

In this final step, we will create the **StoreTruckApp Lambda Function** and **Truck_Queue** to complete the entire streaming analytics pipeline. StoreTruckApp will handle truck information and coordinate deliveries based on analysis results from StorePlanningApp.

## StoreTruckApp Overview

StoreTruckApp is the final component in the streaming analytics architecture:

- **Truck Management**: Manage truck 
- **Delivery Coordination**: Coordinate deliveries based on planning results
- **Route Optimization**: Optimize delivery routes
- **Status Tracking**: Track delivery status in real-time

## Step-by-Step Instructions

### Step 1: Create StoreTruckApp Lambda Function

1. Go to **Lambda Console**
2. Click **"Create function"**
3. Configure function with same settings as previous 2 functions:
   - **Function name**: `StoreTruckApp`
   - **Runtime**: **Python 3.13**
   - **Handler**: `function.lambda_handler`
4. Click **"Create function"**

![Create StoreTruckApp](/images/31.png)

{{% notice info %}}
**StoreTruckApp Purpose**: This function will receive delivery demand information and coordinate delivery trucks optimally.
{{% /notice %}}

### Step 2: Deploy Source Code

1. In the StoreTruckApp code interface
2. Create `function.py` file
3. Copy and paste code from this link: [📁 truck-app-function.py](/downloads/truck-app-function.py)
4. Click **"Deploy"** to deploy code

![Deploy Truck App Code](/images/32.png)

{{% notice download %}}
**📁 Source Code Required**: Copy content from link [truck-app-function.py](/downloads/truck-app-function.py) and paste into the `function.py` file.
{{% /notice %}}

### Step 3: Configure IAM Permissions

1. Navigate to **IAM Console**
2. In the search bar, find the **"StoreTruckApp"** role
3. Select role **"StoreTruckApp-role-xxxxx"**

![Find Truck App Role](/images/32_2.png)

4. **Add permissions** → **"Attach policies"**
5. Attach the following policies:
   - ✅ **AmazonAthenaFullAccess**
   - ✅ **AmazonS3FullAccess** 
   - ✅ **AmazonSQSFullAccess**
   - ✅ **AWSGlueConsoleFullAccess**

![Attach Truck App Policies](/images/32_4.png)

{{% notice info %}}
**Same Permissions**: StoreTruckApp needs the same permissions as StorePlanningApp to query data and send messages.
{{% /notice %}}

### Step 4: Configure Timeout

1. Return to Lambda **"StoreTruckApp"**
2. Go to **"Configuration"** → **"General configuration"**
3. Click **"Edit"**

![Navigate to General Config](/images/32_5.png)

4. Set **Timeout** to **"2 min"** (120 seconds)
5. Click **"Save"** to save

![Set Truck App Timeout](/images/32_6.png)

### Step 5: Create Truck_Queue

1. Navigate to **Amazon SQS Console**
2. Click **"Create queue"**
3. Create queue with same configuration as before:
   - **Queue name**: `Truck_Queue`
   - **Queue type**: **Standard**
   - Keep other settings as default
4. Click **"Create queue"**

![Create Truck Queue](/images/33.png)

{{% notice tip %}}
**Truck_Queue Role**: This queue will receive delivery request messages and trigger StoreTruckApp for processing.
{{% /notice %}}

### Step 6: Configure Environment Variables

1. Return to Lambda **"StoreTruckApp"**
2. Navigate to **"Configuration"** → **"Environment variables"**
3. Click **"Edit"**
4. Add environment variable:
   - **Key**: `queue_url`
   - **Value**: `https://sqs.ap-southeast-1.amazonaws.com/yourID/Truck_Queue`

![Configure Truck App Environment](/images/34.png)

{{% notice warning %}}
**Replace yourID**: Remember to replace `yourID` with your actual AWS Account ID in the Queue URL.
{{% /notice %}}

### Step 7: Test StoreTruckApp Function

1. Go to **"Test"** section of StoreTruckApp
2. Create test event named **"test"**
3. Click **"Test"** button to execute

![Test Truck App](/images/35.png)

## Verify Complete Pipeline

After completing all steps, the streaming analytics system has:

✅ **Data Ingestion**: StoreApp + Kinesis Firehose + S3  
✅ **Data Cataloging**: AWS Glue Database & Table  
✅ **Data Analytics**: Athena queries from StorePlanningApp  
✅ **Message Queuing**: Store_Queue + Truck_Queue  
✅ **Business Logic**: StorePlanningApp + StoreTruckApp  
✅ **End-to-End Flow**: From stores to delivery trucks  

{{% notice success %}}
**🎉 Workshop Complete!** You have successfully completed the Streaming Ingestion & Analytics workshop with a complete serverless architecture on AWS!
{{% /notice %}}

## Workshop Summary

### What we have built:

🏪 **Real-time Data Pipeline**: Collect real-time data from stores  
📊 **Serverless Analytics**: Process and analyze data without server management  
🚛 **Intelligent Routing**: Coordinate delivery trucks based on data analysis  
⚡ **Event-driven Architecture**: Entire system operates on events  
💰 **Cost Optimized**: Pay only when data processing occurs  

### AWS Services Used:

- **AWS Lambda**: Serverless compute for business logic
- **Amazon Kinesis Data Firehose**: Streaming data ingestion  
- **Amazon S3**: Data lake storage
- **AWS Glue**: Data cataloging and ETL
- **Amazon Athena**: Serverless analytics
- **Amazon SQS**: Message queuing
- **IAM**: Security and permissions

### Knowledge Gained:

✅ **Streaming Data Architecture** design patterns  
✅ **Serverless Computing** with AWS Lambda  
✅ **Real-time Analytics** with Kinesis and Athena  
✅ **Event-driven Systems** with SQS  
✅ **Data Lake Architecture** with S3 and Glue  
✅ **Security Best Practices** with IAM  

## Next Steps

Now you can:

1. **Extend Pipeline**: Add more Lambda functions for advanced analytics
2. **Add Monitoring**: Use CloudWatch to monitor the pipeline
3. **Implement Dashboard**: Create visualization with QuickSight
4. **Scale Up**: Apply this pattern for production workloads
5. **Cost Optimization**: Fine-tune resources for cost efficiency

{{% notice tip %}}
**Continue Learning**: Try experimenting with other AWS services like EventBridge, Step Functions, or Elasticsearch to extend this pipeline!
{{% /notice %}}

---

**🎯 Congratulations!** You have mastered building a complete streaming analytics pipeline on AWS!