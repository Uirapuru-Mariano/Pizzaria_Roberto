from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    form_prod = ProdutoForm(request.POST or None)
    if form_prod.is_valid():
        form_prod.save()
        return redirect('index')
    contexto = {
        'form_prod': form_prod
    }

    return render(request, 'cadastro.html', contexto)

def cadastro_cliente(request):
    form_cliente = ClienteForm(request.POST or None)
    if form_cliente.is_valid():
        form_cliente.save()
        return redirect('index')
    contexto = {
        'form_cliente': form_cliente
    }

    return render(request, 'cadastro_cliente.html', contexto)

def cadastro_endereco(request):
    form_endereco = EnderecoForm(request.POST or None)
    if form_endereco.is_valid():
        form_endereco.save()
        return redirect('index')
    contexto = {
        'form_endereco': form_endereco    
    }
        
    return render(request, 'cadastro_endereco.html', contexto)
