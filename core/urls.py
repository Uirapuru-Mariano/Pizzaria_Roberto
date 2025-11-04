from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('login/', login, name='login'),

    path('produtos/', produtos, name='produtos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('edit_produto/<int:id>/', edit_produto, name='edit_produto'),
    path('del_produto/<int:id>/', del_produto, name='del_produto'),

    path("cliente/", cliente, name="cliente"),
    path('cadastro_cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('edit_cliente/<int:id>/', edit_cliente, name='edit_cliente'),
    path('del_cliente/<int:id>/', del_cliente, name='del_cliente'),

    path('endereco/', endereco, name='endereco'),
    path('cadastro_endereco/', cadastro_endereco, name='cadastro_endereco'),
    path('edit_endereco/<int:id>/', edit_endereco, name='edit_endereco'),
    path('del_endereco/<int:id>/', del_endereco, name='del_endereco'),

    path('cadastro_funcionario/', cadastro_funcionario, name='cadastro_funcionario'),

    path('cadastro_pedido/', cadastro_pedido, name='cadastro_pedido'),
    

]