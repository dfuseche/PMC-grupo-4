from django.db import models
from django import forms



# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length= 200)
    correo = models.CharField(max_length = 100)
    contrasenia = models.CharField( max_length = 100)
    descripcion = models.TextField()
     

class Profesor(Usuario):
    carrera = models.CharField(max_length = 100)

class Administrativo(Usuario):
    facultad = models.CharField(max_length = 100)

class Estudiante(Usuario):
    carrera = models.CharField(max_length = 100)
    semestre = models.IntegerField()
    