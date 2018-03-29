import boto3
import os

def lambda_handler(event, context):
    ddb = boto3.client('dynamodb')
    result = ddb.scan(TableName=os.environ['TABLE'], IndexName=os.environ['TABLEINDEX'])
    return result