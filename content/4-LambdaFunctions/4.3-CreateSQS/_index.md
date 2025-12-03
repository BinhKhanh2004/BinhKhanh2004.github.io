---
title : "Create SQS Queue"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 4.3 </b> "
---

In this step, you will create an **Amazon SQS Queue** - a message queue to handle planning requests from the store system. The SQS Queue will serve as a buffer between components in the streaming analytics architecture.

## Amazon SQS Overview

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

### SQS Role in Our System

In our Store Planning architecture, the SQS Queue will:

- **Message Buffer**: Temporarily store messages from the system
- **Decoupling**: Separate data producers from consumers
- **Reliability**: Ensure messages are not lost during processing
- **Scalability**: Automatically scale with message volume

{{% notice info %}}
**SQS in Streaming Pipeline**: The queue will receive messages from various sources and trigger Lambda functions to process planning logic.
{{% /notice %}}

## Step-by-Step Instructions

### Step 1: Navigate to SQS Console

1. In the AWS Console search bar
2. Type **"sqs"**
3. Select **"Simple Queue Service"** from the search results

![Navigate to SQS](/images/21_1.png)

### Step 2: Create New Queue

1. In the SQS Console interface
2. Click the **"Create queue"** button

![Create Queue](/images/21_2.png)

### Step 3: Configure Queue Settings

1. **Queue name**: Name it `Store_Queue`
2. **Queue type**: Keep default **"Standard"**
3. Leave other configurations as default settings
4. Click **"Create queue"** to complete

![Configure Queue](/images/21_3.png)

{{% notice tip %}}
**Standard vs FIFO Queue**: Standard queue provides high throughput and at-least-once delivery, suitable for our streaming analytics use case.
{{% /notice %}}

## Verify Queue Creation

After successful creation, you should see:

✅ **Queue Name**: Store_Queue  
✅ **Queue Type**: Standard  
✅ **Status**: Active  
✅ **Queue URL**: Automatically generated (will be used in next step)  

{{% notice success %}}
**SQS Queue Created!** Store_Queue has been successfully created and is ready to receive messages from the system.
{{% /notice %}}

## Queue URL and Integration

The Queue URL will have the format:
```
https://sqs.ap-southeast-1.amazonaws.com/[YOUR-ACCOUNT-ID]/Store_Queue
```

{{% notice warning %}}
**Note Queue URL**: You will need to copy this Queue URL to configure in the Lambda function in the next step. This URL is the unique identifier for your queue.
{{% /notice %}}


## Preparing for Next Step

Store_Queue is now ready to:

- **Receive messages** from data sources
- **Trigger Lambda function** when new messages arrive
- **Ensure reliability** in message processing

{{% notice info %}}
**Next Step**: In the next step, we will create the "StorePlanningApp" Lambda function that will be triggered by messages from this Store_Queue.
{{% /notice %}}

## Summary

Amazon SQS Store_Queue has been successfully set up with:

- **Reliable message queuing** for store planning system
- **Standard queue type** for high throughput
- **Ready for integration** with Lambda function
- **Scalable architecture** supporting future growth