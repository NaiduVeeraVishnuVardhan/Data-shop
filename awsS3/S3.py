import os

import boto3
from botocore.exceptions import ClientError
from flask import logging


def __get_s3_client():
    return boto3.client('s3',
                        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
                        region_name="ap-southeast-2"
                        )

def upload_file(bucket_name, key_name, file_path):
    print(f"Uploading {file_path} to {bucket_name}/{key_name}")
    try:
        response = __get_s3_client().upload_file(file_path, bucket_name, f"{key_name}/{file_path}")
    except ClientError as e:
        logging.error(e)
        return False