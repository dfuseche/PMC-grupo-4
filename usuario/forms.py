from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        
        model = Usuario
        fields = [
            'username', 'password', 'nombre','edad', 'correo', 'descripcion'
        ]
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'edad': 'Edad',
            'descripcion': 'Descripcion',
            
        }



