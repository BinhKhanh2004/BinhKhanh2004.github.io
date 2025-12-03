---
title : "Streaming Analytics for Store Inventory Management"
weight : 2
chapter : false
---

# Introduction

In this lab, you will build a **streaming analytics system** to monitor store inventory levels and coordinate delivery truck dispatching for restocking.

Store product data is ingested through the **StoreApp** into **Amazon Kinesis Data Firehose**, which streams the data to an **S3 bucket**. You will **manually invoke a Lambda function** to query the data using **Amazon Athena**, analyze inventory levels, and detect which stores need restocking for specific products.

Once the Lambda function is executed, low-inventory alerts will be sent to the **Amazon SQS Queue**, which the **StoreTruckApp** monitors to dispatch delivery trucks to the appropriate store locations.

## Learning Objectives
- Understand how to ingest real-time store data using Amazon Kinesis Data Firehose
- Practice creating and **manually triggering Lambda functions** to process inventory analytics
- Query streaming data stored in S3 using Amazon Athena
- Send delivery coordination messages via Amazon SQS
- Build an end-to-end streaming analytics pipeline for retail operations

## Overall Architecture
![Architecture Diagram](/images/store-inventory-pipeline.png)

1. **Product data** → **StoreApp** streams to **Amazon Kinesis Data Firehose**
2. **Kinesis Data Firehose** → stores data in **S3 bucket** (consumption zone)
3. **Amazon Athena** → queries S3 data for inventory analysis
4. User **manually invokes Lambda** → **StorePlanningApp** processes inventory levels
5. **Lambda** → detects stores with low inventory and sends alerts to **Amazon SQS Queue**
6. **StoreTruckApp** → consumes SQS messages and coordinates **Delivery** trucks
7. **Delivery trucks** → restock stores based on inventory needs

{{% notice info %}}
**Key Point**: Unlike fully automated systems, you will manually trigger the Lambda function to process inventory data and coordinate deliveries. This gives you hands-on control over the analytics pipeline.
{{% /notice %}}