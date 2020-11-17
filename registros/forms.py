from django import forms
from .models import *


class RegistroForm(forms.ModelForm):
    file=forms.FileField()
    class Meta:
        model = Registro
        fields = [
            'titulo',
            'autor',
            'talla',
            'precio',
            
            
        ]

        labels = {
            'titulo': 'Nombre',
            'autor': 'Descripción',
            'talla': 'Talla',
            'precio': 'Precio',
            'file':'Archivo',
            'nombre':'a',

        }
        exclude={'url',}



