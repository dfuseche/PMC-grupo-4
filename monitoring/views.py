from django.shortcuts import render
from registros.models import Registro
from usuario.models import Usuario

def index(request):
    return render(request, 'index.html')

def perfil_usuario(request):
    usuarios = get_usuarios(Usuario)
    usuarioRegistrado = request.user
    usuarioHerencia = request.user
    registros = get_registros(Registro)
    registrosDelusuario=[]
    for x in usuarios: 
        if x.username == usuarioRegistrado.username:
            usuarioHerencia = x
            
    for y in registros: 
        if y.propietario == usuarioRegistrado:
            registrosDelusuario.append(y)
            
           

    
    usuarioRegistrado = request.user
    
    context = {'usuarioRegistrado': usuarioRegistrado,
                'usuarioHerencia': usuarioHerencia,
                'registrosDelusuario': registrosDelusuario,}
    return render(request, 'accounts/profile.html', context)

def get_registros(tipo):
    queryset = tipo.objects.all()
    return (queryset)

def get_usuarios(tipo):
    queryset = tipo.objects.all()
    return (queryset)
