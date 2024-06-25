# s3-file-metadata-sync

This project provides a Lambda function to sync the metadata of an uploaded file in S3 to DynamoDB.

## Setting Up the Project

### Step 1: Set Up AWS Environment

1. **Create an S3 bucket to upload your files.**

2. **Create a DynamoDB table named `s3MetadataServerless` to store the metadata. Ensure it has a primary key attribute named `Resource_id`.**

3. **Create an IAM Role for Lambda and Attach the following policies:**
   - `AmazonS3ReadOnlyAccess`
   - `AmazonDynamoDBFullAccess`
   - `AWSLambdaBasicExecutionRole`

### Step 2: Create the Lambda Function

- **Create the Lambda Function by adding the code to Lambda.**
- **Replace the default code by deploying the `lambda_function.py` script to AWS Lambda.**

### Step 3: Configure S3 Trigger

- **Go to the Lambda function configuration and click on Add trigger.**
- **Select S3 as the trigger source. Choose the S3 bucket created earlier.**
- **Set the event type to All object create events (or any specific events such as `s3:ObjectCreated:*`).**

### Step 4: Test the Setup

- **Open the S3 console and navigate to your bucket.**
- **Upload a test file to the bucket.**

### Step 5: Check DynamoDB

- **Open the DynamoDB console and navigate to your table (`s3MetadataServerless`).**
- **Click on the Explore table items button.**
- **If you see no items returned, then use Scan or query items option and select Scan and press Run.**
- **Now you see the data in the items returned section.**
- **Verify that a new item has been added with the correct metadata.**

## Additional Resources

For a detailed step-by-step guide, please refer to [my blog post](https://tonythomas.in/how-to-sync-the-metadata-of-an-uploaded-file-in-s3-to-dyanamodb-using-lamda/).
