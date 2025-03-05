# AWS Glue Job with S3 Lifecycle Policy, SNS Notification, and S3 Inventory

## Project Overview
This project demonstrates how to set up an **AWS Glue Job** for daily incremental data load from one S3 bucket to another. It leverages **SNS notifications** for job status alerts, **S3 Lifecycle Policies** to manage object versions automatically, and **S3 Inventory** with **Athena** for auditing object activities.

### 🔥 Key Features
- Automated **AWS Glue ETL Job** for daily incremental data load.
- Data movement from **`s3://backup-data-1-data/`** to **`s3://test-lifecyclepolicy-bucket-delete/Data/Data1/`**.
- **SNS notifications** for job completion status.
- **Scheduled Triggers** at **6 AM** and **4 PM (UTC)** daily.
- **S3 Lifecycle Policy** to automatically delete expired versions and retain **2 latest versions**.
- **S3 Inventory Setup** to track object activities.
- **Athena Integration** to query inventory data.

---
## Folder Structure

Glue-job/
├─ scripts/
│   └─ glue_job_script.py       # Glue Job ETL Script
└─ README.md                  # Documentation

---
## How to Deploy

### 1. Clone the Repository
```bash
git clone https://github.com/AmitDevops007/Glue-job.git
cd Glue-job
```
### 2. Upload Script to S3
Upload **`glue_job_script.py`** to your S3 bucket path where AWS Glue will fetch the script.

### 3. Verify Glue Job
- Navigate to **AWS Glue Console**.
- Confirm the creation of the **`daily_incremental_load_job`** job.
- Check if the **scheduled triggers** are set for **6 AM** and **4 PM (UTC)**.

### 4. Setup S3 Inventory
- Enable **S3 Inventory** on the target bucket.
- Configure the inventory to generate reports in CSV format.

### 5. Run Glue Crawler
- Configure AWS Glue Crawler to read **S3 Inventory Reports**.
- Use **AWS Glue Classifier** to parse CSV files.
- Create a table in **Athena** to query the inventory data.

### 6. Testing SNS Notification
- Upload files to **`s3://backup-data-1-data/`**.
- Wait for the scheduled Glue job execution.
- You will receive an **SNS notification** with the job execution summary.
- Use Athena to query inventory changes.

---
## Tech Stack
- AWS Glue
- AWS S3
- AWS SNS
- S3 Lifecycle Policies
- S3 Inventory
- AWS Athena
- Python

---
## Author
**Amit Raj**


