from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('cadastro_user/', cadastro_user, name='cadastro_user'),

    path('produtos/', produtos, name='produtos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('edit_produto/<int:id>/', edit_produto, name='edit_produto'),
    path('del_produto/<int:id>/', del_produto, name='del_produto'),

    path('endereco/', endereco, name='endereco'),
    path('cadastro_endereco/', cadastro_endereco, name='cadastro_endereco'),
    path('edit_endereco/<int:id>/', edit_endereco, name='edit_endereco'),
    path('del_endereco/<int:id>/', del_endereco, name='del_endereco'),

    path('pedido/', pedido, name='pedido'),
    path('cadastro_pedido/', cadastro_pedido, name='cadastro_pedido'),
    path('edit_pedido/<int:id>/', edit_pedido, name='edit_pedido'),
    path('del_pedido//<int:id>', del_pedido, name='del_pedido'),
    

]