import boto3
import os
import pandas as pd

BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_KEY_ID = os.environ['S3_KEY_ID']
S3_KEY_SECRET = os.environ['S3_KEY_SECRET']

s3 = boto3.resource(
    service_name='s3',
    region_name='sa-east-1',
    aws_access_key_id=S3_KEY_ID,
    aws_secret_access_key=S3_KEY_SECRET
)
for bucket in s3.buckets.all():
    print(bucket.name)

filename= "myjson.json"
people = pd.DataFrame({"name":"Jose carlos","preferences":["bread","apple"]})
people.to_json(filename)

s3.Bucket(BUCKET_NAME).upload_file(Filename=filename, Key=filename)

print("File uploaded with success")
os.remove(filename)

print("File removed with success")