import boto3
from decouple import config


ACCESS_ID = config("s3_access")
SECRET_KEY = config("s3_secret")


def delete_bucket(workout_id: int):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY)
    bucket = s3.Bucket('videos-bucket-0001')
    response = bucket.objects.filter(Prefix=str(workout_id) + '/').delete()
    return not (response == [])
