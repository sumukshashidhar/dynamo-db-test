import boto3
import json

with open('rootkey.csv', 'r') as f:
    ls = f.readlines()
ls = [x[:-1] for x in ls] 
print(ls)


dynamodb = boto3.client("dynamodb", region_name="ap-south-1", aws_access_key_id=ls[0], aws_secret_access_key=ls[1])


response = dynamodb.describe_table(TableName="TEST_TABLE")
print(response["Table"])

response2 = dynamodb.


print("Connection successful")


