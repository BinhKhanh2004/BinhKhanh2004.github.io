---
title : "Create Database & Table"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

In this step, you will create an AWS Glue database and table that will serve as the metadata catalog for your streaming inventory data. This catalog enables Amazon Athena to understand and query the data stored in your S3 consumption bucket.

## Overview

AWS Glue Data Catalog acts as a centralized metadata repository that stores information about your data's structure, format, and location. When you create a database and table in Glue, you're essentially creating a schema that Athena can use to interpret your raw data files.

**What we'll create:**
- **Database**: `conversion_db` - Logical container for our inventory tables
- **Table**: `conversion_table` - Schema definition for inventory data structure

## Part A: Creating the Glue Database

### Step 1: Navigate to AWS Glue Console

1. From the **AWS Management Console** home page, locate the search bar at the top
2. Type **"Glue"** in the search field
3. Click on **"AWS Glue"** from the search results

![Navigate to AWS Glue](/images/0_4.png)

### Step 2: Access Databases Section

1. In the AWS Glue console, look at the left navigation panel
2. Find and click on **"Databases"** under the Data Catalog section
3. In the Databases page, click the **"Add database"** button located in the top-right corner

![AWS Glue Navigation](/images/0_5.png)

### Step 3: Create the Database

1. In the **Database name** field, enter: `conversion_db`
2. Leave other settings as default
3. Click **"Create database"** to complete the creation

![Create Glue Database](/images/0_6.png)

{{% notice success %}}
**Success!** You have successfully created the `conversion_db` database. This database will serve as the logical container for our inventory data tables.
{{% /notice %}}

## Part B: Creating the Glue Table

### Step 4: Navigate to Tables Section

1. In the left navigation panel, under **"Databases"**, click on **"Tables"**
2. Click the **"Add table"** button in the top-right corner

![Navigate to Tables](/images/0_7.png)

### Step 5: Configure Table Basic Information

1. **Table name**: Enter `conversion_table`
2. **Database**: Select `conversion_db` from the dropdown (the database we just created)
3. Leave other basic settings as default

![Configure Table](/images/0_8.png)

### Step 6: Configure Data Store

1. Scroll down to the **"Include path"** section
2. Click **"Browse S3"** or manually enter the path to your S3 bucket:
   ```
   s3://consumption-bucket-yourname/
   ```
   {{% notice info %}}
   Replace "yourname" with the actual name you used when creating your S3 bucket in step 2.1
   {{% /notice %}}

3. In the **"Data format"** section, select **"Parquet"**
4. Click **"Next"** to proceed

![Configure Table Data Store](/images/0_9.png)

### Step 7: Define Schema Using JSON

1. On the schema definition page, select **Edit schema as JSON**
2. Copy the schema content from this link: [📁 inventory-schema.json](/downloads/inventory-schema.json)
3. Paste the copied JSON content into the **Edit schema as JSON** field
4. Click **"Save"** to apply the schema

![Edit Schema as JSON](/images/0_10.png)
![Finalize Table Creation](/images/0_11.png)

{{% notice warning %}}
Schema Content Required: You must copy the exact JSON schema from the provided link above. This pre-defined schema matches the inventory data structure that will be streamed from your StoreApp. Do not modify the schema content as it needs to match the incoming data format.
{{% /notice %}}

### Step 8: Finalize Table Creation

1. Review your table configuration
2. Click **"Next"** to proceed to the final step
3. Review the summary and click **"Create table"** to complete

![Glue Database and Table Created](/images/0_12.png)

## Verification

After successful creation, you should see:
- Database: `conversion_db` in the Databases list
- Table: `conversion_table` under the `conversion_db` database

![Review Table](/images/0_13.png)

{{% notice success %}}
**Congratulations!** You have successfully created both the Glue database and table. Amazon Athena can now use this metadata catalog to query your streaming inventory data.
{{% /notice %}}
