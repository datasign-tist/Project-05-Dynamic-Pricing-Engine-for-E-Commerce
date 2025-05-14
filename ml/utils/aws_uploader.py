import boto3

def upload_to_s3(local_file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(local_file_path, bucket_name, s3_key)
