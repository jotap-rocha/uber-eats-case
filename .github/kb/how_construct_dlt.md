Tutorial: Build an ETL pipeline using change data capture
Learn how to create and deploy an ETL (extract, transform, and load) pipeline with change data capture (CDC) using Lakeflow Spark Declarative Pipelines (SDP) for data orchestration and Auto Loader. An ETL pipeline implements the steps to read data from source systems, transform that data based on requirements, such as data quality checks and record de-duplication, and write the data to a target system, such as a data warehouse or a data lake.

In this tutorial, you'll use data from a customers table in a MySQL database to:

Extract the changes from a transactional database using Debezium or another tool and save them to cloud object storage (S3, ADLS, or GCS). In this tutorial, you skip setting up an external CDC system and instead generate fake data to simplify the tutorial.
Use Auto Loader to incrementally load the messages from cloud object storage, and store the raw messages in the customers_cdc table. Auto Loader infers the schema and handles schema evolution.
Create the customers_cdc_clean table to check data quality using expectations. For example, the id should never be null because it's used to run upsert operations.
Perform AUTO CDC ... INTO on the cleaned CDC data to upsert changes into the final customers table.
Show how a pipeline can create a type 2 slowly changing dimension (SCD2) table to track all changes.
The goal is to ingest the raw data in near real time and build a table for your analyst team while ensuring data quality.

The tutorial uses the medallion Lakehouse architecture, where it ingests raw data through the bronze layer, cleans and validates data with the silver layer, and applies dimensional modeling and aggregation using the gold layer. See What is the medallion lakehouse architecture? for more information.

The implemented flow looks like this:

Pipeline with CDC

For more information about pipeline, Auto Loader, and CDC see Lakeflow Spark Declarative Pipelines, What is Auto Loader?, and What is change data capture (CDC)?

Requirements
To complete this tutorial, you must meet the following requirements:

Be logged in to a Databricks workspace.
Have Unity Catalog enabled for your workspace.
Have serverless compute enabled for your account. Serverless Lakeflow Spark Declarative Pipelines is not available in all workspace regions. See Features with limited regional availability for available regions. If serverless compute is not enabled for your account, the steps should work with the default compute for your workspace.
Have permission to create a compute resource or access to a compute resource.
Have permissions to create a new schema in a catalog. The required permissions are ALL PRIVILEGES or USE CATALOG and CREATE SCHEMA.
Have permissions to create a new volume in an existing schema. The required permissions are ALL PRIVILEGES or USE SCHEMA and CREATE VOLUME.
Change data capture in an ETL pipeline
Change data capture (CDC) is the process that captures changes in records made to a transactional database (for example, MySQL or PostgreSQL) or a data warehouse. CDC captures operations like data deletes, appends, and updates, typically as a stream to re-materialize tables in external systems. CDC enables incremental loading while eliminating the need for bulk-load updates.

note
To simplify this tutorial, skip setting up an external CDC system. Assume it's running and saving CDC data as JSON files in cloud object storage (S3, ADLS, or GCS). This tutorial uses the Faker library to generate the data used in the tutorial.

Capturing CDC
A variety of CDC tools are available. One of the leading open source solutions is Debezium, but other implementations that simplify data sources exist, such as Fivetran, Qlik Replicate, StreamSets, Talend, Oracle GoldenGate, and AWS DMS.

In this tutorial, you use CDC data from an external system like Debezium or DMS. Debezium captures every changed row. It typically sends the history of data changes to Kafka topics or saves them as files.

You must ingest the CDC information from the customers table (JSON format), check that it is correct, and then materialize the customers table in the Lakehouse.

CDC input from Debezium
For each change, you receive a JSON message containing all the fields of the row being updated (id, firstname, lastname, email, address). The message also includes additional metadata:

operation: An operation code, typically (DELETE, APPEND, UPDATE).
operation_date: The date and timestamp for the record for each operation action.
Tools like Debezium can produce more advanced output, such as the row value before the change, but this tutorial omits them for simplicity.

Step 1: Create a pipeline
Create a new ETL pipeline to query your CDC data source and generate tables in your workspace.

In your workspace, click Plus icon. New in upper-left corner.

Click ETL Pipeline.

Change the title of the pipeline to Pipelines with CDC tutorial or a name you prefer.

Under the title, choose a catalog and schema for which you have write permissions.

This catalog and schema are used by default, if you do not specify a catalog or schema in your code. Your code can write to any catalog or schema by specifying the full path. This tutorial uses the defaults that you specify here.

From Advanced options, select Start with an empty file.

Choose a folder for your code. You can select Browse to browse the list of folders in the workspace. You can choose any folder for which you have write permissions.

To use version control, select a Git folder. If you need to create a new folder, select the Plus icon. button.

Choose Python or SQL for the language of your file, based on the language you want to use for the tutorial.

Click Select to create the pipeline with these settings and open the Lakeflow Pipelines Editor.

You now have a blank pipeline with a default catalog and schema. Next, set up the sample data to import in the tutorial.

Step 2: Create the sample data to import in this tutorial
This step is not needed if you are importing your own data from an existing source. For this tutorial, generate fake data as an example for the tutorial. Create a notebook to run the Python data generation script. This code only needs to be run once to generate the sample data, so create it within the pipeline's explorations folder, which is not run as part of a pipeline update.

note
This code uses Faker to generate the sample CDC data. Faker is available to install automatically, so the tutorial uses %pip install faker. You can also set a dependency on faker for the notebook. See Add dependencies to the notebook.

From within the Lakeflow Pipelines Editor, in the asset browser sidebar to the left of the editor, click Plus icon. Add, then choose Exploration.

Give it a Name, such as Setup data, select Python. You can leave the default destination folder, which is a new explorations folder.

Click Create. This creates a notebook in the new folder.

Enter the following code in the first cell. You must change the definition of <my_catalog> and <my_schema> to match the default catalog and schema that you selected in the previous procedure:

Python
%pip install faker
# Update these to match the catalog and schema
# that you used for the pipeline in step 1.
catalog = "<my_catalog>"
schema = dbName = db = "<my_schema>"

spark.sql(f'USE CATALOG `{catalog}`')
spark.sql(f'USE SCHEMA `{schema}`')
spark.sql(f'CREATE VOLUME IF NOT EXISTS `{catalog}`.`{db}`.`raw_data`')
volume_folder =  f"/Volumes/{catalog}/{db}/raw_data"

try:
  dbutils.fs.ls(volume_folder+"/customers")
except:
  print(f"folder doesn't exist, generating the data under {volume_folder}...")
  from pyspark.sql import functions as F
  from faker import Faker
  from collections import OrderedDict
  import uuid
  fake = Faker()
  import random

  fake_firstname = F.udf(fake.first_name)
  fake_lastname = F.udf(fake.last_name)
  fake_email = F.udf(fake.ascii_company_email)
  fake_date = F.udf(lambda:fake.date_time_this_month().strftime("%m-%d-%Y %H:%M:%S"))
  fake_address = F.udf(fake.address)
  operations = OrderedDict([("APPEND", 0.5),("DELETE", 0.1),("UPDATE", 0.3),(None, 0.01)])
  fake_operation = F.udf(lambda:fake.random_elements(elements=operations, length=1)[0])
  fake_id = F.udf(lambda: str(uuid.uuid4()) if random.uniform(0, 1) < 0.98 else None)

  df = spark.range(0, 100000).repartition(100)
  df = df.withColumn("id", fake_id())
  df = df.withColumn("firstname", fake_firstname())
  df = df.withColumn("lastname", fake_lastname())
  df = df.withColumn("email", fake_email())
  df = df.withColumn("address", fake_address())
  df = df.withColumn("operation", fake_operation())
  df_customers = df.withColumn("operation_date", fake_date())
  df_customers.repartition(100).write.format("json").mode("overwrite").save(volume_folder+"/customers")


To generate the dataset used in the tutorial, type Shift + Enter to run the code:

Optional. To preview the data used in this tutorial, enter the following code in the next cell and run the code. Update the catalog and schema to match the path from the previous code.

Python
# Update these to match the catalog and schema
# that you used for the pipeline in step 1.
catalog = "<my_catalog>"
schema = "<my_schema>"

display(spark.read.json(f"/Volumes/{catalog}/{schema}/raw_data/customers"))

This generates a large data set (with fake CDC data) that you can use in the rest of the tutorial. In the next step, ingest the data using Auto Loader.

Step 3: Incrementally ingest data with Auto Loader
The next step is to ingest the raw data from the (faked) cloud storage into a bronze layer.

This can be challenging for multiple reasons, as you must:

Operate at scale, potentially ingesting millions of small files.
Infer schema and JSON type.
Handle bad records with incorrect JSON schema.
Take care of schema evolution (for example, a new column in the customer table).
Auto Loader simplifies this ingestion, including schema inference and schema evolution, while scaling to millions of incoming files. Auto Loader is available in Python using cloudFiles and in SQL using the SELECT * FROM STREAM read_files(...) and can be used with a variety of formats (JSON, CSV, Apache Avro, etc.):

Defining the table as a streaming table guarantees that you only consume new incoming data. If you do not define it as a streaming table, it scans and ingests all the available data. See Streaming tables for more information.

To ingest the incoming CDC data using Auto Loader, copy and paste the following code into the code file that was created with your pipeline (called my_transformation.py). You can use Python or SQL, based on the language you chose when creating the pipeline. Be sure to replace the <catalog> and <schema> with the ones that you set up for the default for the pipeline.

Python
SQL
Python
from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Replace with the catalog and schema name that
# you are using:
path = "/Volumes/<catalog>/<schema>/raw_data/customers"


# Create the target bronze table
dp.create_streaming_table("customers_cdc_bronze", comment="New customer data incrementally ingested from cloud object storage landing zone")

# Create an Append Flow to ingest the raw data into the bronze table
@dp.append_flow(
  target = "customers_cdc_bronze",
  name = "customers_bronze_ingest_flow"
)
def customers_bronze_ingest_flow():
  return (
      spark.readStream
          .format("cloudFiles")
          .option("cloudFiles.format", "json")
          .option("cloudFiles.inferColumnTypes", "true")
          .load(f"{path}")
  )


Click Play icon. Run file or Run pipeline to start an update for the connected pipeline. With only one source file in your pipeline, these are functionally equivalent.

When the update completes, the editor is updated with information about your pipeline.

The pipeline graph (DAG), in the sidebar to the right of your code, shows a single table, customers_cdc_bronze.
A summary of the update is shown at the top of the pipeline assets browser.
Details of the table that was generated are shown in the bottom pane, and you can browse data from the table by selecting it.
This is the raw bronze layer data imported from cloud storage. In the next step, clean the data to create a silver layer table.

Step 4: Cleanup and expectations to track data quality
After the bronze layer is defined, create the silver layer by adding expectations to control data quality. Check the following conditions:

ID must never be null.
The CDC operation type must be valid.
JSON must be read correctly by Auto Loader.
Rows that don't meet these conditions are dropped.

See Manage data quality with pipeline expectations for more information.

From the pipeline assets browser sidebar, click Plus icon. Add, then Transformation.

Enter a Name and choose a language (Python or SQL) for the source code file. You can mix and match languages within a pipeline, so you can choose either one for this step.

To create a silver layer with a cleansed table and impose constraints, copy and paste the following code into the new file (choose Python or SQL based on the language of the file).

Python
SQL
Python
from pyspark import pipelines as dp
from pyspark.sql.functions import *

dp.create_streaming_table(
  name = "customers_cdc_clean",
  expect_all_or_drop = {"no_rescued_data": "_rescued_data IS NULL","valid_id": "id IS NOT NULL","valid_operation": "operation IN ('APPEND', 'DELETE', 'UPDATE')"}
  )

@dp.append_flow(
  target = "customers_cdc_clean",
  name = "customers_cdc_clean_flow"
)
def customers_cdc_clean_flow():
  return (
      spark.readStream.table("customers_cdc_bronze")
          .select("address", "email", "id", "firstname", "lastname", "operation", "operation_date", "_rescued_data")
  )


Click Play icon. Run file or Run pipeline to start an update for the connected pipeline.

Because there are now two source files, these do not do the same thing, but in this case, the output is the same.

Run pipeline runs your entire pipeline, including the code from step 3. If your input data were being updated, this would pull in any changes from that source to your bronze layer. This does not run the code from the data setup step, because that is in the explorations folder, and not part of the source for your pipeline.
Run file runs only the current source file. In this case, without your input data being updated, this generates the silver data from the cached bronze table. It would be useful to run just this file for faster iteration when creating or editing your pipeline code.
When the update completes, you can see that the pipeline graph now shows two tables (with the silver layer depending on the bronze layer), and the bottom panel shows details for both tables. The top of the pipeline assets browser now shows multiple runs' times, but only details for the most recent run.

Next, create your final gold layer version of the customers table.

Step 5: Materialize the customers table with an AUTO CDC flow
Up to this point, the tables have just passed the CDC data along in each step. Now, create the customers table to both contain the most up-to-date view and to be a replica of the original table, not the list of CDC operations that created it.

This is nontrivial to implement manually. You must consider things like data deduplication to keep the most recent row.

However, Lakeflow Spark Declarative Pipelines solves these challenges with the AUTO CDC operation.

From the pipeline assets browser sidebar, click Plus icon. Add and Transformation.

Enter a Name and choose a language (Python or SQL) for the new source code file. You can again choose either language for this step, but use the correct code, below.

To process the CDC data using AUTO CDC in Lakeflow Spark Declarative Pipelines, copy and paste the following code into the new file.

Python
SQL
Python
from pyspark import pipelines as dp
from pyspark.sql.functions import *

dp.create_streaming_table(name="customers", comment="Clean, materialized customers")

dp.create_auto_cdc_flow(
  target="customers",  # The customer table being materialized
  source="customers_cdc_clean",  # the incoming CDC
  keys=["id"],  # what we'll be using to match the rows to upsert
  sequence_by=col("operation_date"),  # de-duplicate by operation date, getting the most recent value
  ignore_null_updates=False,
  apply_as_deletes=expr("operation = 'DELETE'"),  # DELETE condition
  except_column_list=["operation", "operation_date", "_rescued_data"],
)


Click Play icon. Run file to start an update for the connected pipeline.

When the update is complete, you can see that your pipeline graph shows 3 tables, progressing from bronze to silver to gold.

Step 6: Track update history with slowly changing dimension type 2 (SCD2)
It's often required to create a table tracking all the changes resulting from APPEND, UPDATE, and DELETE:

History: You want to keep a history of all the changes to your table.
Traceability: You want to see which operation occurred.
SCD2 with Lakeflow SDP
Delta supports change data flow (CDF), and table_change can query table modifications in SQL and Python. However, CDF's main use case is to capture changes in a pipeline, not to create a full view of table changes from the beginning.

Things get especially complex to implement if you have out-of-order events. If you must sequence your changes by a timestamp and receive a modification that happened in the past, you must append a new entry in your SCD table and update the previous entries.

Lakeflow SDP removes this complexity and lets you create a separate table that contains all modifications from the beginning of time. This table can then be used at scale, with specific partitions or ZORDER columns if required. Out-of-order fields are handled out of the box based on the _sequence_by.

To create an SCD2 table, use the option STORED AS SCD TYPE 2 in SQL or stored_as_scd_type="2" in Python.

note
You can also limit which columns the feature tracks using the option: TRACK HISTORY ON {columnList | EXCEPT(exceptColumnList)}

From the pipeline assets browser sidebar, click Plus icon. Add and Transformation.

Enter a Name and choose a language (Python or SQL) for the new source code file.

Copy and paste the following code into the new file.

Python
SQL
Python
from pyspark import pipelines as dp
from pyspark.sql.functions import *

# create the table
dp.create_streaming_table(
    name="customers_history", comment="Slowly Changing Dimension Type 2 for customers"
)

# store all changes as SCD2
dp.create_auto_cdc_flow(
    target="customers_history",
    source="customers_cdc_clean",
    keys=["id"],
    sequence_by=col("operation_date"),
    ignore_null_updates=False,
    apply_as_deletes=expr("operation = 'DELETE'"),
    except_column_list=["operation", "operation_date", "_rescued_data"],
    stored_as_scd_type="2",
)  # Enable SCD2 and store individual updates

Click Play icon. Run file to start an update for the connected pipeline.

When the update is complete, the pipeline graph includes the new customers_history table, also dependent on the silver layer table, and the bottom panel shows the details for all 4 tables.

Step 7: Create a materialized view that tracks who has changed their information the most
The table customers_history contains all historical changes a user has made to their information. Create a simple materialized view in the gold layer that keeps track of who has changed their information the most. This could be used for fraud detection analysis or user recommendations in a real-world scenario. Additionally, applying changes with SCD2 has already removed duplicates, so you can directly count the rows per user ID.

From the pipeline assets browser sidebar, click Plus icon. Add and Transformation.

Enter a Name and choose a language (Python or SQL) for the new source code file.

Copy and paste the following code into the new source file.

Python
SQL
Python
from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
  name = "customers_history_agg",
  comment = "Aggregated customer history"
)
def customers_history_agg():
  return (
    spark.read.table("customers_history")
      .groupBy("id")
      .agg(
          count("address").alias("address_count"),
          count("email").alias("email_count"),
          count("firstname").alias("firstname_count"),
          count("lastname").alias("lastname_count")
      )
  )

Click Play icon. Run file to start an update for the connected pipeline.

After the update is complete, there is a new table in the pipeline graph that depends on the customers_history table, and you can view it in the bottom panel. Your pipeline is now complete. You can test it by performing a full Run pipeline. The only steps left are to schedule the pipeline to update regularly.

Step 8: Create a job to run the ETL pipeline
Next, create a workflow to automate the data ingestion, processing, and analysis steps in your pipeline using a Databricks job.

At the top of the editor, choose the Schedule button.
If the Schedules dialog appears, choose Add schedule.
This opens the New schedule dialog, where you can create a job to run your pipeline on a schedule.
Optionally, give the job a name.
By default, the schedule is set to run once per day. You can accept this default, or set your own schedule. Choosing Advanced gives you the option to set a specific time that the job will run. Selecting More options allows you to create notifications when the job runs.
Select Create to apply the changes and create the job.
Now the job will run daily to keep your pipeline up to date. You can choose Schedule again to view the list of schedules. You can manage schedules for your pipeline from that dialog, including adding, editing, or removing schedules.

Clicking the name of the schedule (or job) takes you to the job's page in the Jobs & pipelines list. From there you can view details about job runs, including the history of runs, or run the job immediately with the Run now button.

See Monitoring and observability for Lakeflow Jobs for more information about job runs.

Lakeflow Spark Declarative Pipelines Python language reference
This section has details for the Lakeflow Spark Declarative Pipelines (SDP) Python programming interface.

For conceptual information and an overview of using Python for pipelines, see Develop pipeline code with Python.
For SQL reference, see the Pipeline SQL language reference.
For details specific to configuring Auto Loader, see What is Auto Loader?.
pipelines module overview
Lakeflow Spark Declarative Pipelines Python functions are defined in the pyspark.pipelines module (imported as dp). Your pipelines implemented with the Python API must import this module:

Python
from pyspark import pipelines as dp

note
The pipelines module is only available in the context of a pipeline. It is not available in Python running outside of pipelines. For more information about editing pipeline code, see Develop and debug ETL pipelines with the Lakeflow Pipelines Editor.

Apache Spark™ pipelines
Apache Spark includes declarative pipelines beginning in Spark 4.1, available through the pyspark.pipelines module. The Databricks Runtime extends these open source capabilities with additional APIs and integrations for managed production use.

Code written with the open-source pipelines module runs without modification on Databricks. The following features are not part of Apache Spark:

dp.create_auto_cdc_flow
dp.create_auto_cdc_from_snapshot_flow
@dp.expect(...)
@dp.temporary_view
The pipelines module was previously called dlt in Databricks. For details, and more information about the differences from Apache Spark, see What happened to @dlt?.

Functions for dataset definitions
Pipelines use Python decorators for defining datasets such as materialized views and streaming tables. See Functions to define datasets.

API reference
append_flow
create_auto_cdc_flow
create_auto_cdc_from_snapshot_flow
create_sink
create_streaming_table
Expectations
materialized_view
table
temporary_view
Coding requirements for Python pipelines
The following are important requirements when you implement pipelines with the Lakeflow Spark Declarative Pipelines (SDP) Python interface:

SDP evaluates the code that defines a pipeline multiple times during planning and pipeline runs. Python functions that define datasets should include only the code required to define the table or view. Arbitrary Python logic included in dataset definitions might lead to unexpected behavior.
Do not try to implement custom monitoring logic in your dataset definitions. See Define custom monitoring of pipelines with event hooks.
The function used to define a dataset must return a Spark DataFrame. Do not include logic in your dataset definitions that does not relate to a returned DataFrame.
Never use methods that save or write to files or tables as part of your pipeline dataset code.
Examples of Apache Spark operations that should never be used in pipeline code:

collect()
count()
toPandas()
save()
saveAsTable()
start()
toTable()
What happened to @dlt?
Previously, Databricks used the dlt module to support pipeline functionality. The dlt module has been replaced by the pyspark.pipelines module. You may still use dlt, but Databricks recommends using pipelines.

Differences between DLT, SDP, and Apache Spark
The following table shows the differences in syntax and functionality between DLT, Lakeflow Spark Declarative Pipelines, and Apache Spark Declarative Pipelines.

Area

DLT syntax

SDP Syntax (Lakeflow and Apache, where applicable)

Available in Apache Spark

Imports

import dlt

from pyspark import pipelines (as dp, optionally)

Yes

Streaming table

@dlt.table with a streaming dataframe

@dp.table

Yes

Materialized view

@dlt.table with a batch dataframe

@dp.materialized_view

Yes

View

@dlt.view

@dp.temporary_view

Yes

Append flow

@dlt.append_flow

@dp.append_flow

Yes

SQL – streaming

CREATE STREAMING TABLE ...

CREATE STREAMING TABLE ...

Yes

SQL – materialized

CREATE MATERIALIZED VIEW ...

CREATE MATERIALIZED VIEW ...

Yes

SQL – flow

CREATE FLOW ...

CREATE FLOW ...

Yes

Event log

spark.read.table("event_log")

spark.read.table("event_log")

No

Apply Changes (CDC)

dlt.apply_changes(...)

dp.create_auto_cdc_flow(...)

No

Expectations

@dlt.expect(...)

dp.expect(...)

No

Continuous mode

Pipeline config with continuous trigger

(same)

No

Sink

@dlt.create_sink(...)

dp.create_sink(...)

Yes


Manage data quality with pipeline expectations
Use expectations to apply quality constraints that validate data as it flows through ETL pipelines. Expectations provide greater insight into data quality metrics and allow you to fail updates or drop records when detecting invalid records.

This article has an overview of expectations, including syntax examples and behavior options. For more advanced use cases and recommended best practices, see Expectation recommendations and advanced patterns.

Pipeline expectations flow graph

What are expectations?
Expectations are optional clauses in pipeline materialized view, streaming table, or view creation statements that apply data quality checks on each record passing through a query. Expectations use standard SQL Boolean statements to specify constraints. You can combine multiple expectations for a single dataset and set expectations across all dataset declarations in a pipeline.

The following sections introduce the three components of an expectation and provide syntax examples.

Expectation name
Each expectation must have a name, which is used as an identifier to track and monitor the expectation. Choose a name that communicates the metrics being validated. The following example defines the expectation valid_customer_age to confirm that age is between 0 and 120 years:

important
An expectation name must be unique for a given dataset. You can reuse expectations across multiple datasets in a pipeline. See Portable and reusable expectations.

Python
SQL
Python
@dp.table
@dp.expect("valid_customer_age", "age BETWEEN 0 AND 120")
def customers():
  return spark.readStream.table("datasets.samples.raw_customers")

Constraint to evaluate
The constraint clause is a SQL conditional statement that must evaluate to true or false for each record. The constraint contains the actual logic for what is being validated. When a record fails this condition, the expectation is triggered.

Constraints must use valid SQL syntax and cannot contain the following:

Custom Python functions
External service calls
Subqueries referencing other tables
The following are examples of constraints that could be added to dataset creation statements:

Python
SQL
The syntax for a constraint in Python is:

Python
@dp.expect(<constraint-name>, <constraint-clause>)

Multiple constraints can be specified:

Python
@dp.expect(<constraint-name>, <constraint-clause>)
@dp.expect(<constraint2-name>, <constraint2-clause>)

Examples:

Python
# Simple constraint
@dp.expect("non_negative_price", "price >= 0")

# SQL functions
@dp.expect("valid_date", "year(transaction_date) >= 2020")

# CASE statements
@dp.expect("valid_order_status", """
   CASE
     WHEN type = 'ORDER' THEN status IN ('PENDING', 'COMPLETED', 'CANCELLED')
     WHEN type = 'REFUND' THEN status IN ('PENDING', 'APPROVED', 'REJECTED')
     ELSE false
   END
""")

# Multiple constraints
@dp.expect("non_negative_price", "price >= 0")
@dp.expect("valid_purchase_date", "date <= current_date()")

# Complex business logic
@dp.expect(
  "valid_subscription_dates",
  """start_date <= end_date
    AND end_date <= current_date()
    AND start_date >= '2020-01-01'"""
)

# Complex boolean logic
@dp.expect("valid_order_state", """
   (status = 'ACTIVE' AND balance > 0)
   OR (status = 'PENDING' AND created_date > current_date() - INTERVAL 7 DAYS)
""")

Action on invalid record
You must specify an action to determine what happens when a record fails the validation check. The following table describes the available actions:

Action

SQL syntax

Python syntax

Result

warn (default)

EXPECT

dp.expect

Invalid records are written to the target.

drop

EXPECT ... ON VIOLATION DROP ROW

dp.expect_or_drop

Invalid records are dropped before data is written to the target. The count of dropped records is logged alongside other dataset metrics.

fail

EXPECT ... ON VIOLATION FAIL UPDATE

dp.expect_or_fail

Invalid records prevent the update from succeeding. Manual intervention is required before reprocessing. This expectation causes a failure of a single flow and does not cause other flows in your pipeline to fail.

You can also implement advanced logic to quarantine invalid records without failing or dropping data. See Quarantine invalid records.

Expectation tracking metrics
You can see tracking metrics for warn or drop actions from the pipeline UI. Because fail causes the update to fail when an invalid record is detected, metrics are not recorded.

To view expectation metrics, complete the following steps:

In your Databricks workspace's sidebar, click Jobs & Pipelines.
Click the Name of your pipeline.
Click a dataset with an expectation defined.
Select the Data quality tab in the right sidebar.
You can view data quality metrics by querying the Lakeflow Spark Declarative Pipelines event log. See Query data quality or expectations metrics.

Retain invalid records
Retaining invalid records is the default behavior for expectations. Use the expect operator when you want to keep records that violate the expectation but collect metrics on how many records pass or fail a constraint. Records that violate the expectation are added to the target dataset along with valid records:

Python
SQL
Python
@dp.expect("valid timestamp", "timestamp > '2012-01-01'")

Drop invalid records
Use the expect_or_drop operator to prevent further processing of invalid records. Records that violate the expectation are dropped from the target dataset:

Python
SQL
Python
@dp.expect_or_drop("valid_current_page", "current_page_id IS NOT NULL AND current_page_title IS NOT NULL")


Fail on invalid records
When invalid records are unacceptable, use the expect_or_fail operator to stop execution immediately when a record fails validation. If the operation is a table update, the system atomically rolls back the transaction:

Python
SQL
Python
@dp.expect_or_fail("valid_count", "count > 0")

important
If you have multiple parallel flows defined in a pipeline, failure of a single flow does not cause other flows to fail.

LDP flow failure explanation graph

Troubleshooting failed updates from expectations
When a pipeline fails because of an expectation violation, you must fix the pipeline code to handle the invalid data correctly before re-running the pipeline.

Expectations configured to fail pipelines modify the Spark query plan of your transformations to track information required to detect and report violations. You can use this information to identify which input record resulted in the violation for many queries. Lakeflow Spark Declarative Pipelines provides a dedicated error message to report such violations. Here's an example of an expectation violation error message:

Console
[EXPECTATION_VIOLATION.VERBOSITY_ALL] Flow 'sensor-pipeline' failed to meet the expectation. Violated expectations: 'temperature_in_valid_range'. Input data: '{"id":"TEMP_001","temperature":-500,"timestamp_ms":"1710498600"}'. Output record: '{"sensor_id":"TEMP_001","temperature":-500,"change_time":"2024-03-15 10:30:00"}'. Missing input data: false


Multiple expectations management
note
While both SQL and Python support multiple expectations in a single dataset, only Python allows you to group multiple expectations and specify collective actions.

LDP with multiple expectations fLow graph

You can group multiple expectations together and specify collective actions using the functions expect_all, expect_all_or_drop, and expect_all_or_fail.

These decorators accept a Python dictionary as an argument, where the key is the expectation name and the value is the expectation constraint. You can reuse the same set of expectations in multiple datasets in your pipeline. The following shows examples of each of the expect_all Python operators:

Python
valid_pages = {"valid_count": "count > 0", "valid_current_page": "current_page_id IS NOT NULL AND current_page_title IS NOT NULL"}

@dp.table
@dp.expect_all(valid_pages)
def raw_data():
  # Create a raw dataset

@dp.table
@dp.expect_all_or_drop(valid_pages)
def prepared_data():
  # Create a cleaned and prepared dataset

@dp.table
@dp.expect_all_or_fail(valid_pages)
def customer_facing_data():
  # Create cleaned and prepared to share the dataset


Limitations
Because only streaming tables and materialized views support expectations, data quality metrics are supported only for these object types.
Data quality metrics are not available when:
No expectations are defined on a query.
A flow uses an operator that does not support expectations.
The flow type, such as sinks, does not support expectations.
There are no updates to the associated streaming table or materialized view for a given flow run.
The pipeline configuration does not include the necessary settings for capturing metrics, such as pipelines.metrics.flowTimeReporter.enabled.
For some cases, a COMPLETED flow might not contain metrics. Instead, metrics are reported in each micro-batch in a flow_progress event with the status RUNNING.