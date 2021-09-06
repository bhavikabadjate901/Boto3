import os
import sys
import datetime
import time
import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee')

table.put_item(
	Item={
		'emp_id':"2",
		'name': "Badjate",
		'age': "24"
	}
)

res = table.get_item(
	Key ={
		'emp_id':"1"
	}
)

print(res["Item"])
