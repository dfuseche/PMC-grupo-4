from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('registros/', views.registro_list),
    path('registroCreate/', csrf_exempt(views.registro_create), name='registroCreate'),
   
]