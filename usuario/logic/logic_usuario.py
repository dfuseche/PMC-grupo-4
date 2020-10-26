from ..models import Usuario
from ..models import Estudiante
from ..models import Administrativo
from ..models import Profesor
from monitoring.settings import AWS_STORAGE_BUCKET_NAME
from monitoring.settings import AWS_S3_REGION_NAME
from monitoring.settings import AWS_SECRET_ACCESS_KEY
from monitoring.settings import AWS_ACCESS_KEY_ID
from botocore import UNSIGNED
import boto3
import os
from botocore.config import Config

def get_usuarios():
    queryset = Usuario.objects.all()
    get_user_keys()
    return (queryset)

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_administrativos():
    queryset = Administrativo.objects.all()
    return (queryset)

def get_profesores():
    queryset = Profesor.objects.all()
    return (queryset)

def create_usuario(form):
    usuario = form.save()
    usuario.save()
    return ()

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()

def create_administrativo(form):
    administrativo = form.save()
    administrativo.save()
    return ()

def create_profesor(form):
    profesor = form.save()
    profesor.save()
    return ()

def get_user_keys():
    queryset = Usuario.objects.all().values_list('id', flat=True)
    keys = open('./usuario/static/userkeys.txt', 'w')
    for id in queryset:
        keys.write(str(id) + '\n')
    keys.close()
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    bucket.upload_file('./usuario/static/userkeys.txt','userkeys.txt',
      ExtraArgs={'ACL': 'public-read'})
    return