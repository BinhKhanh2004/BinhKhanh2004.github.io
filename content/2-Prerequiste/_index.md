---
title : "Preparation"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

In this module, you will prepare the foundational infrastructure components needed for our streaming analytics pipeline. These components will serve as the backbone for data storage, processing, and analysis throughout the workshop.

## Infrastructure Components Overview

Before we can start streaming and analyzing store inventory data, we need to set up:

1. **S3 Consumption Bucket** - Data lake storage for streamed inventory records
2. **IAM Role for Kinesis Data Firehose** - Permissions for data delivery to S3
3. **Conversion Database** - AWS Glue Data Catalog database for organizing our data
4. **Conversion Table** - Glue table structure that Athena will use for querying inventory data

## Why These Components Matter

### S3 Consumption Bucket
Acts as your **data lake** where all streaming inventory data from stores will be stored. This bucket serves as the central repository that Amazon Athena will query for analytics.

### IAM Role for Firehose
Ensures **secure data delivery** from Kinesis Data Firehose to your S3 bucket. Without proper permissions, the streaming pipeline cannot function.

### Conversion Database & Table
Creates the **metadata catalog** in AWS Glue Data Catalog that defines the schema for your inventory data. Amazon Athena uses this Glue catalog to understand the structure of your S3 data, enabling SQL queries on raw JSON inventory records. The database serves as a logical container, while the table definition maps JSON fields to queryable columns.

{{% notice info %}}
**Preparation Time**: This module should take approximately 15-20 minutes to complete all setup tasks.
{{% /notice %}}

{{% notice warning %}}
**Important**: Complete all preparation steps in order. Each component depends on the previous ones being properly configured.
{{% /notice %}}

### Workshop Content
  - [Create S3 Consumption Bucket](2.1-create-s3-bucket/)  
  - [Create IAM Role for Kinesis Data Firehose](2.2-create-firehose-role/)  
  - [Create Conversion Database in AWS Glue Data Catalog](2.3-create-glue-database/)  
  - [Create Conversion Table in AWS Glue Data Catalog](2.4-create-glue-table/)

Once you complete this preparation phase, you'll have a solid foundation to build your streaming analytics pipeline for store inventory management.