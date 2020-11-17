from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .logic.logic_usuario import *
from django.shortcuts import redirect

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



