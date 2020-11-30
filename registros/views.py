from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.registro_logic import *
from usuario.models import Usuario

def registro_list(request):
    queryset = request.GET.get("buscar")
    registros = get_registros(Registro)
    if queryset:
       
        
        registros = Registro.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(autor__icontains = queryset) |
            Q(talla__icontains = queryset)   |
            Q(precio__icontains = queryset) 
        ).distinct()
    
    
    context = {
        'registro_list': registros
    }
    
    return render(request, 'registros.html', context)


def registro_create(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST,request.FILES)
        if form.is_valid():
            create_registro(form, request)
            messages.add_message(request, messages.SUCCESS, 'Registro create successful')
            return HttpResponseRedirect(reverse('registroCreate'))
        else:
            print(form.errors)
    else:
        form = RegistroForm()

    context = {
        'form': form,
    }

    return render(request, 'registroCreate.html', context)

def delete_registro(request, pk):
    obj = get_object_or_404(Registro, pk = pk)
    if request.method == "POST":
        obj.delete()
        print("entro")
        return redirect('../')
    print("no entro")
    return render(request, "registroDelete.html", {"object": obj})
def get_listaUsuarios(tipo):
    queryset = tipo.objects.all()
    return (queryset)

def registro_detail(request, pk):
    registro = get_object_or_404(Registro, pk = pk)
    usuario = request.user
    usuarios2 = get_listaUsuarios(Usuario)
    usuarios = get_listaUsuarios(User)
    usuarioHerencia = request.user
    registrosCombinaciones = get_registros(Registro)
    nombre = registro.titulo
    nombreSplit = nombre.split()
    for x in usuarios: 
        if x.username == pk:
            usuarioHerencia = x
    for z in usuarios2: 
        if z.pk == usuarioHerencia.pk:
            usuario = z
    
    registrosCombinaciones = Registro.objects.filter(
            Q(titulo__icontains = nombreSplit[1])  
        ).distinct()
    registroCombinaciones = registrosCombinaciones.exclude(titulo = nombre)
   
    registrosCombinaciones.exclude(titulo = registro.titulo)
       
            
    return render(request, "registroDetail.html", {"registros": registroCombinaciones,'usuario':usuario,'usuarioHerencia': usuarioHerencia, "registro": registro})