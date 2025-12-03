---
title : " Lambda Functions"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

In this section, you will learn about **AWS Lambda Functions** and their role in the streaming analytics architecture. Lambda will play a crucial role in processing real-time data from stores and sending notifications to the delivery truck management system.

## AWS Lambda Overview

AWS Lambda is a **serverless** computing service that lets you run code without provisioning or managing servers. Lambda automatically scales your application by running code in response to each trigger, automatically managing the underlying compute resources.

### Why Use Lambda in Streaming Data Pipeline?

In the context of our store inventory management system, Lambda serves as a **real-time data processor**:

- **Data Generator**: Creates simulated inventory data from multiple different stores
- **Streaming Integration**: Sends data directly to Kinesis Data Firehose
- **Event-Driven**: Can be triggered manually or on a schedule
- **JSON Format**: Generates data with JSON structure compatible with Glue table schema

## StoreApp Lambda Function Features

The StoreApp Lambda function will simulate retail stores sending inventory information such as:

✅ **Store ID and Location**: Store identification and location details  
✅ **Product Information**: ID, name, and product category  
✅ **Stock Levels**: Current inventory vs minimum threshold comparison  
✅ **Timestamps**: Time stamps for real-time tracking  

{{% notice info %}}
**Lambda in Streaming Analytics**: Lambda function serves as a crucial intermediary, receiving data from sources and transforming it before sending to Kinesis Data Firehose.
{{% /notice %}}

## Lambda Advantages in Our System

### ⚡ **Serverless Computing**
- No infrastructure management required
- AWS handles all provisioning and scaling
- Focus on business logic instead of server management

### 📈 **Auto-scaling**
- Automatically scales with traffic
- Handles from few requests to thousands of requests/second
- No capacity planning configuration needed

### 💰 **Cost-effective**
- Pay only when code executes
- No charges when idle
- Pricing model based on requests and compute time

### 🔄 **Event-driven**
- Responds immediately to events
- Integrates with multiple AWS services
- Supports real-time data processing

{{% notice warning %}}
**Important Note**: The Lambda function in this workshop will be triggered **manually** so you can observe and understand each step of the data processing pipeline.
{{% /notice %}}

## Summary

AWS Lambda is the core component in our streaming analytics architecture. It provides:

- **Real-time processing capability** for store data
- **Seamless integration** with Kinesis Data Firehose  
- **Serverless architecture** that reduces complexity
- **Cost optimization** with pay-per-use model

Let's start by creating the StoreApp Lambda Function in the next step!