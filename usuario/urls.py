from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('usuarios/', views.usuario_list),
    path('estudiantes/', views.estudiante_list),
    path('administrativos/', views.administrativo_list),
    path('profesores/', views.profesor_list),
    path('usuarioCreate/', csrf_exempt(views.usuario_create), name='usuarioCreate'),
    path('estudianteCreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
    path('profesorCreate/', csrf_exempt(views.profesor_create), name='profesorCreate'),
    path('administrativoCreate/', csrf_exempt(views.administrativo_create), name='administrativoCreate'),
    path('estudiantes/<int:pk>/', csrf_exempt(views.estudiante_detail), name='estudianteDetail'),
    path('estudiantes/<int:pk>/edit/', views.estudiante_edit, name='estudianteCreate'),
    path('administrativos/<int:pk>/', csrf_exempt(views.administrativo_detail), name='administrativoDetail'),
    path('administrativos/<int:pk>/edit/', views.administrativo_edit, name='administrativoCreate'),
    path('profesores/<int:pk>/', csrf_exempt(views.profesor_detail), name='profesorDetail'),
    path('profesores/<int:pk>/edit/', views.profesor_edit, name='profesorCreate'),
    
]