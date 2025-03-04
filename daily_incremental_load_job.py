import sys
import boto3
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime

# Create Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Hardcoded Values
job_name = "daily_incremental_load_job"
sns_topic_arn = "arn:aws:sns:us-east-1:423623831602:Glue-Job-Notification"
s3_source_path = "s3://backup-data-1-data/"
s3_target_path = "s3://test-lifecyclepolicy-bucket-delete/Data/Data1/"

# Initialize Job
job.init(job_name, {})

# Boto3 Clients for S3 and SNS
s3 = boto3.client("s3")
sns = boto3.client("sns")

# List Objects in Source Bucket
response = s3.list_objects_v2(Bucket="backup-data-1-data")
uploaded_files = []

if 'Contents' in response:
    for obj in response['Contents']:
        source_key = obj['Key']
        target_key = f"Data/Data1/{source_key}"
        s3.copy_object(Bucket="test-lifecyclepolicy-bucket-delete", CopySource={"Bucket": "backup-data-1-data", "Key": source_key}, Key=target_key)
        uploaded_files.append(target_key)
        print(f"{target_key} uploaded successfully")
else:
    print("No files found in source bucket")

# Send SNS Notification
if uploaded_files:
    message = f"Glue Job completed successfully. Uploaded files: {', '.join(uploaded_files)}"
    sns.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject="Glue Job Notification"
    )
    print("SNS Notification sent")

print(f"Files uploaded successfully to {s3_target_path}")

# Commit Job
job.commit()
