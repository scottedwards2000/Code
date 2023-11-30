# Function to upload a file to an S3 bucket

import boto3
import logging


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print('xxx')
        print(response)

    except Exception as e:
        #logging.error(e)
        print('s')
        print(e)
        return False
    return True


if __name__ == '__main__':
    upload_file('questions', 'scottedwards2000')
#    print("File uploaded successfully")
