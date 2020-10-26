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

def estudiante_list(request):
    estudiantes = get_estudiantes()
    context = {
        'estudiante_list': estudiantes
    }
    return render(request, 'estudiantes.html', context)

def administrativo_list(request):
    administrativos = get_administrativos()
    context = {
        'administrativo_list': administrativos
    }
    return render(request, 'administrativos.html', context)

def profesor_list(request):
    profesores = get_profesores()
    context = {
        'profesor_list': profesores
    }
    return render(request, 'profesores.html', context)

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            create_estudiante(form)
            messages.add_message(request, messages.SUCCESS, 'Estudiante creado con éxito')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()

    context = {
        'form': form,
    }
    return render(request, 'estudianteCreate.html', context)


def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            create_profesor(form)
            messages.add_message(request, messages.SUCCESS, 'Profesor creado con éxito')
            return HttpResponseRedirect(reverse('profesorCreate'))
        else:
            print(form.errors)
    else:
        form = ProfesorForm()

    context = {
        'form': form,
    }
    return render(request, 'profesorCreate.html', context)

def administrativo_create(request):
    if request.method == 'POST':
        form = AdministrativoForm(request.POST)
        if form.is_valid():
            create_administrativo(form)
            messages.add_message(request, messages.SUCCESS, 'Administrativo creado con éxito')
            return HttpResponseRedirect(reverse('administrativoCreate'))
        else:
            print(form.errors)
    else:
        form = AdministrativoForm()

    context = {
        'form': form,
    }
    return render(request, 'administrativoCreate.html', context)

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


def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudianteDetail.html', {'estudiante':estudiante })

def estudiante_edit(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            create_estudiante(form)
            messages.add_message(request, messages.SUCCESS, 'Estudiante actualizado con éxito')
            return HttpResponseRedirect(reverse('estudianteCreate'))
    else:
        form =EstudianteForm(instance=estudiante)
    context = {
        'form': form,
    }    
    return render(request, 'estudianteCreate.html', context)

    

def administrativo_detail(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    return render(request, 'administrativoDetail.html', {'administrativo':administrativo })

def administrativo_edit(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    if request.method == "POST":
        form = AdministrativoForm(request.POST, instance=administrativo)
        if form.is_valid():
            create_administrativo(form)
            messages.add_message(request, messages.SUCCESS, 'Administrativo actualizado con éxito')
            return HttpResponseRedirect(reverse('administrativoCreate'))
    else:
        form =AdministrativoForm(instance=administrativo)
    context = {
        'form': form,
    }  
    return render(request, 'administrativoCreate.html', context)

def profesor_detail(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'profesorDetail.html', {'profesor':profesor })

def profesor_edit(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            create_profesor(form)
            messages.add_message(request, messages.SUCCESS, 'Profesor actualizado con éxito')
            return HttpResponseRedirect(reverse('profesorCreate'))
    else:
        form =ProfesorForm(instance=profesor)
    context = {
        'form': form,
    }  
    return render(request, 'profesorCreate.html', context)
