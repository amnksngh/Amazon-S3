import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region = None):
    """Assumes bucket_name and region two strings
       Creates an S3 bucket in a specified region
       Returns True if the bukcet is created or False
    
    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1)"""

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket = bucket_name)
        else:
            s3_client = boto3.client('s3')
            location = {'LocationConstraint' : region}
            s3_client.create_bucket(Bucket = bucket_name,
                                    CreateBucketConfiguration = location)
            
    except ClientError as e:
        loggin.error(e)
        return False
    return True

# create_bucket('Data')

# Retrive the list of existing buckets

s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'    {bucket["Name"]}')