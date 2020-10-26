from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.registro_logic import *

def registro_list(request):
    registros = get_registros(Registro)
    context = {
        'registro_list': registros
    }
    
    return render(request, 'registros.html', context)


def registro_create(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST,request.FILES)
        if form.is_valid():
            create_registro(form)
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

