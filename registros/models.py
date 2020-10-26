from django.db import models


class Registro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=300, editable=False)
    autor = models.CharField(max_length=80)

    def __str__(self):
        return '%s de %s' % (self.titulo, self.autor)


