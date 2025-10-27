from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_endereco', cadastro_endereco, name='cadastro_endereco'),

]