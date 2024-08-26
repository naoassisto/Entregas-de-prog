import os
import boto3
import pytest
from moto import mock_aws
from modulo.storage import upload_to_s3

@pytest.fixture(scope='module')
def s3():
    with mock_aws():
        os.environ['AWS_ACCESS_KEY_ID'] = 'test'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
        s3 = boto3.resource('s3')
        s3.create_bucket(Bucket='test_bucket')
        yield s3

def test_upload_to_s3(s3):
    upload_to_s3("test data", "test_bucket", "test.txt")

    # Verify that the file was uploaded
    obj = s3.Object('test_bucket', 'test.txt')
    body = obj.get()['Body'].read().decode('utf-8')
    assert body == "test data"
