AWS Glue Job with CloudFormation and SNS Notification

Project Overview

This project demonstrates how to set up an AWS Glue Job for daily incremental data load from one S3 bucket to another, 
using AWS CloudFormation for infrastructure automation and SNS notifications for job status alerts.

Features Implemented😎:
1>AWS Glue ETL Job for daily incremental data load
2>Data movement from s3://backup-data-1-data/ to s3://test-lifecyclepolicy-bucket-delete/Data/Data1/
3>SNS notifications to send job success notifications
4>CloudFormation template for automated infrastructure setup
5>Scheduled trigger at 6 AM  and 4 PM (UTC) daily using Glue Trigger
6> Added a lifecycle policy in bucket s3://test-lifecyclepolicy-bucket-delete to delete versioned file and retrive 2 versions

Folder Structure:

Glue-job/
├─ scripts/
│   └─ glue_job_script.py       # Glue Job ETL Script
├─ templates/
│   └─ cloudformation_template.json # CloudFormation Template
└─ README.md                  # Documentation


How to Deploy
1. Clone the Repository
git clone https://github.com/AmitDevops007/Glue-job.git
cd Glue-job

2. Upload Script to S3
Upload glue_job_script.py into your S3 bucket where AWS Glue will pick the script from.

3. Deploy CloudFormation Stack
Use AWS CLI or AWS Console to deploy the CloudFormation template:

aws cloudformation create-stack \
  --stack-name GlueJobStack \
  --template-body file://templates/cloudformation_template.json \
  --capabilities CAPABILITY_NAMED_IAM

4. Verify Glue Job
Go to AWS Glue Console
Check if the job daily_incremental_load_job is created
Verify the trigger schedule
5. Testing SNS Notification

Upload files to s3://backup-data-1-data/ and wait for the scheduled run.
SNS will notify the job status.

Tech Stack
1.AWS Glue
2.AWS S3
3.AWS SNS
4.AWS CloudFormation
5.S3 Life cycle
6.Python

Author:
Amit Raj

License:
This project is licensed under the MIT License.


In future will add more features

