import boto3
import botocore
import itertools
import csv
from collections import Counter

# TASK: prepare a web service that reads first 100 lines from a file stored on S3, parses it and returns number of players in each team.
#
# Below is a script that gets the object from S3. It can be helpful when creating full, object-oriented solution


BUCKET_NAME = 'interview-ihs'
KEY = 'mlb_players.csv'

# Documentation for Boto3 client:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/boto3.html
client = boto3.client(
    's3',
    aws_access_key_id='',
    aws_secret_access_key=''
)

try:
    # See: https://botocore.amazonaws.com/v1/documentation/api/latest/reference/response.html
    stream = client.get_object(Bucket=BUCKET_NAME, Key=KEY)['Body']
    # ...
    
    
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
