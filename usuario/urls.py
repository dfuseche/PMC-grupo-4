from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('usuarios/', views.usuario_list),
    path('usuarioCreate/', csrf_exempt(views.usuario_create), name='usuarioCreate'),
    path('usuarios/<str:pk>/', csrf_exempt(views.usuario_detail), name='usuarioDetail'),
    
    
]