import boto3
import os

def lambda_handler(event, context):
    ddb = boto3.client('dynamodb')
    result = ddb.get_item(
        TableName=os.environ['TABLE'],
        Key={
            'routeID':{'S':str(event['params']['routeID'])}
        }
    )
    if result.get("Item"):
        return result
    else:
        raise Exception ("Route Not Found")