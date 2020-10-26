from ..models import *
from monitoring.settings import AWS_STORAGE_BUCKET_NAME
from monitoring.settings import AWS_S3_REGION_NAME
from monitoring.settings import AWS_SECRET_ACCESS_KEY
from monitoring.settings import AWS_ACCESS_KEY_ID
from botocore import UNSIGNED
from botocore.client import Config
import boto3
import os

def get_registros(tipo):
    queryset = tipo.objects.all()
    return (queryset)

def create_registro(form):
    registro = form.save(commit=False)
    file = form.cleaned_data['file']
    registro.url = upload_file_s3(file)
    registro.save()
    return ()


def upload_file_s3(file):
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    filename=os.path.basename(file.name)
    bucket.upload_fileobj(file,filename,
      ExtraArgs={'ACL': 'public-read'})
    url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{filename}"
    return url

def get_keys_s3():
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    keys = open('./registros/static/keys.txt', 'w')
    for file in bucket.objects.all():
        key = file.key
        keys.write(key + '\n')
    keys.close()
    return