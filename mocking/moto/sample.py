import boto3
from moto import mock_s3,mock_secretsmanager
import json


myBucket = "my_test_bucket"
myPrefix = "mockS3"
fixturesPath = "tests/fixtures"
clickStreamFile = "test_eventClickStreamSample_data.csv"
clickStreamOnlyProcessFile = "test_eventClickStreamSample_process.csv"


class SecretManagerClass:
    def __init__(self, secretName, secretValue):
        self.name = secretName
        self.value = secretValue

    def createSecret(self):
        client = boto3.client('secretsmanager')
        client.put_secret_value(
            SecretId=self.name, SecretString='["username":"check123","password":"check13333"]',)

    def fetchSecret(self):
        client = boto3.client('secretsmanager')
        response = client.get_secret_value(SecretId=self.name)
        print(response)


class MyModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)


@mock_s3
@mock_secretsmanager
def test_my_model_save():
    """
        S3 package 
    """ 
    # conn = boto3.client('s3', region_name='us-east-1')
    # conn.create_bucket(Bucket='mybucket')
    # s3 = boto3.resource("s3")
    # myBucket = s3.Bucket('mybucket')
    # # We need to create the bucket since this is all in Moto's 'virtual' AWS account

    # # myBucket = conn.Bucket('mybucket')

    # model_instance = MyModel('steve/', 'is awesome')
    # model_instance.save()
    # model_instance = MyModel('test/check/', 'is awesome')
    # model_instance.save()

    # tempVar = conn.list_objects(Bucket='mybucket')
    # # buckets = conn.list_buckets()['Buckets']
    # # print(str(buckets))
    # print(tempVar["Contents"])


    # # print(list(myBucket.objects.all()))
    # # print(list(myBucket.objects.filter(Prefix='steve/')))
    # # print(conn.list_objects())
    # # body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")
    """
        Secret Manager
    """
    sec=SecretManagerClass("new","ceckekcek")
    sec.createSecret()
    sec.fetchSecret()
    
if __name__ == "__main__":
    test_my_model_save()
