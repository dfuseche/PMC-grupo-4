from django import forms
from .models import Usuario, Estudiante, Administrativo, Profesor

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre', 'correo', 'contrasenia','descripcion'
        ]
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'contrasenia' : 'Contraseña',
            'descripcion': 'Descripcion',
            
        }



class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre', 'correo', 'descripcion', 'carrera', 'semestre',
        ]
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'descripcion': 'Descripcion',
            'carrera': 'Carrera',
            'semestre': 'Semestre',
        }

class AdministrativoForm(forms.ModelForm):
    class Meta:
        model = Administrativo
        fields = [
            'nombre', 'correo', 'descripcion', 'facultad',
        ]
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'descripcion': 'Descripcion',
            'facultad': 'Facultad',
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            'nombre', 'correo', 'descripcion', 'carrera',
        ]
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'descripcion': 'Descripcion',
            'carrera': 'Carrera',
        }