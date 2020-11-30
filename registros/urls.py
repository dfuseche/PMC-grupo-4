from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('registros/', views.registro_list),
    path('registroCreate/', csrf_exempt(views.registro_create), name='registroCreate'),
    path('accounts/profile/<int:pk>/delete', views.delete_registro, name='registro-delete'),
    path('registros/<int:pk>/', csrf_exempt(views.registro_detail), name='registroDetail'),
]