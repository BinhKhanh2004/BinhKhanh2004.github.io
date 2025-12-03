---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

**Streaming Analytics** is an AWS solution for collecting, storing, and processing real-time data from various sources. In this workshop, we will apply it to the scenario of **store inventory management and delivery coordination**.

Each store sends its product inventory data through the **StoreApp** into **Amazon Kinesis Data Firehose**, which streams the data to an **S3 bucket** for storage. The user will then **manually invoke a Lambda function** (StorePlanningApp) to query the data using **Amazon Athena**, analyze inventory levels, and detect which stores are running low on specific products. The results will then be sent through **Amazon SQS** to notify the **StoreTruckApp**, which coordinates delivery trucks for restocking.

### Advantages of this approach
Compared to traditional inventory management methods, AWS Streaming Analytics provides several benefits:

- **Real-time inventory monitoring** with data lake storage instead of waiting for periodic reports
- **Serverless Lambda processing** with Athena analytics, eliminating the need to manage servers or databases
- **Scalable data ingestion via Kinesis Data Firehose**, able to handle data from hundreds of stores simultaneously
- **Reliable message queuing with SQS**, ensuring delivery coordination messages are not lost
- **Cost-effective analytics**, you only pay for the data processed and queries executed
- **Flexible data storage in S3**, enabling historical analysis and machine learning capabilities

### Architecture Components Integration
- **StoreApp**: Collects and streams inventory data from retail locations
- **Kinesis Data Firehose**: Reliably ingests streaming data to S3 with automatic scaling
- **S3 Consumption Zone**: Serves as a data lake for inventory records
- **Amazon Athena**: Provides serverless SQL analytics on S3 data
- **StorePlanningApp (Lambda)**: Processes inventory analytics and triggers alerts
- **Amazon SQS**: Manages delivery coordination message queue
- **StoreTruckApp**: Monitors SQS and dispatches delivery trucks

With these integrated components, the Streaming Analytics system enables more efficient supply chain management, reduces the risk of stock shortages, improves delivery coordination, and enhances overall customer satisfaction through better inventory availability.