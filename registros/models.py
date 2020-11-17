from django.db import models
from django.contrib.auth.models import User


class Registro(models.Model):
    propietario = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=300, editable=False)
    autor = models.CharField(max_length=80)
    precio = models.IntegerField()
    talla = models.CharField(max_length=10)
  


    def __str__(self):
        return '%s de %s' % (self.nombre, self.vendedor)


1