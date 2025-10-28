from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login, name='login'),

    path('cadastro/', cadastro, name='cadastro'),
    path('edit_produto/<int:id>/', edit_produto, name='edit_produto'),

    path('cadastro_cliente/', cadastro_cliente, name='cadastro_cliente'),

    path('cadastro_endereco/', cadastro_endereco, name='cadastro_endereco'),

    path('cadastro_funcionario', cadastro_funcionario, name='cadastro_funcionario'),

    path('cadastro_pedido/', cadastro_pedido, name='cadastro_pedido'),
    

]