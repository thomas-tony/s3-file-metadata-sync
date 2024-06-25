import boto3
from uuid import uuid4

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client("s3")
    
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    
    # Iterate over each record in the event
    for record in event['Records']:
        # Get the bucket name from the event record
        bucket_name = record['s3']['bucket']['name']
        
        # Get the object key (file name) from the event record
        object_key = record['s3']['object']['key']
        
        # Get the size of the object from the event record, defaulting to -1 if not present
        size = record['s3']['object'].get('size', -1)
        
        # Get the event name (e.g., ObjectCreated:Put) from the event record
        event_name = record['eventName']
        
        # Get the event time from the event record
        event_time = record['eventTime']
        
        # Specify the DynamoDB table name
        dynamoTable = dynamodb.Table('s3MetadataServerless')
        
        # Put the item into the DynamoDB table
        dynamoTable.put_item(
            Item={
                'Resource_id': str(uuid4()),  # Unique identifier for the resource
                'Bucket': bucket_name,        # Name of the S3 bucket
                'Object': object_key,         # Key (name) of the S3 object
                'Size': size,                 # Size of the S3 object
                'Event': event_name,          # Name of the event (e.g., ObjectCreated:Put)
                'EventTime': event_time       # Time of the event
            }
        )
