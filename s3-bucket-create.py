'''This script leverage boto3 for CRUD operations on S3.

#Configure cli authentication and install boto3
!aws configure set aws_access_key_id {}
!aws configure set aws_secret_access_key {}
!aws configure set region us-east-1
!aws configure set output json
!aws --version
!pip install boto3'''

import boto3

#Create a bucket and check if it already exists
s3 = boto3.resource('s3')
bucket_name = 'dct-crudmd-1'

all_my_buckets = [bucket.name for bucket in s3.buckets.all()]

if bucket_name not in all_my_buckets:
  print(f"'{bucket_name}' doesn't exit. Creating now..")
  s3.create_bucket(Bucket=bucket_name)
  print(f"{bucket_name} bucket has been created.")
else:
  print(f"{bucket_name} alread exists.")

#load a file into bucket
file_1 = '/content/file_1.text'
file_2 = '/content/file_2.text'

s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)

#Ready content of file
obj = s3.Object(bucket_name, file_1)
print(obj.get()['Body'].read())

#Open file and update conent from file2 
s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))
print(obj.get()['Body'].read())

#Delete file and bucket
s3.Object(bucket_name, file_1).delete()
bucket = s3.Bucket(bucket_name)
bucket.delete()
