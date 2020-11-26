from django.db import models
from django import forms
from django.contrib.auth.models import User



# Create your models here.
class Usuario(User):
    nombre = models.CharField(max_length= 200)
    correo = models.CharField(max_length = 100)
    descripcion = models.TextField()
    edad = models.IntegerField()
  
     


    