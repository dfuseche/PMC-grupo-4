from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .logic.logic_usuario import *
from django.shortcuts import redirect
from registros.models import Registro
from django.contrib.auth.models import User

def usuario_list(request):
    usuarios = get_usuarios()
    context = {
        'usuario_list': usuarios
    }
    return render(request, 'usuarios.html', context)



def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            create_usuario(form)
            messages.add_message(request, messages.SUCCESS, 'Usuario create successful')
            return HttpResponseRedirect(reverse('usuarioCreate'))
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'usuarioCreate.html', context)
def get_registros(tipo):
    queryset = tipo.objects.all()
    return (queryset)
def get_listaUsuarios(tipo):
    queryset = tipo.objects.all()
    return (queryset)

def usuario_detail(request, pk):
    print(pk)
    usuario = request.user
    usuarios2 = get_listaUsuarios(Usuario)
    registros = get_registros(Registro)
    usuarios = get_listaUsuarios(User)
    usuarioHerencia = request.user
    registrosDelusuario=[]
    
    for x in usuarios: 
        if x.username == pk:
            usuarioHerencia = x
    for z in usuarios2: 
        if z.pk == usuarioHerencia.pk:
            usuario = z
         
    for y in registros: 
        print(y.propietario)
        if y.propietario == usuarioHerencia:
            registrosDelusuario.append(y)
        
            
        
    
    return render(request, 'usuarioDetail.html', {'usuario':usuario, 'registrosDelusuario': registrosDelusuario, 'usuarioHerencia': usuarioHerencia })
