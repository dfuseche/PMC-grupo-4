from django import forms
from .models import *


class RegistroForm(forms.ModelForm):
    file=forms.FileField()
    class Meta:
        model = Registro
        fields = [
            'titulo',
            'autor',
        ]

        labels = {
            'titulo': 'Nombre',
            'autor': 'vendedor',
            'file':'Archivo',
            'nombre':'a',
        }
        exclude={'url',}



