from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('crear_tablero', views.form_tablero , name='crear_tablero'),
  

    
]