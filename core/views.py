from django.shortcuts import render, redirect
from .forms import *
from .models import *

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

def produtos(request):
    lista_produto = Produto.objects.all()

    contexto = {

        'lista_produto': lista_produto
    }

    return render(request, 'produtos.html', contexto)

def cadastro(request):
    form_prod = ProdutoForm(request.POST or None)
    if form_prod.is_valid():
        form_prod.save()
        return redirect('produtos')
    contexto = {
        'form_prod': form_prod, 'texto': 'Cadastrar Produto'
    }

    return render(request, 'cadastro.html', contexto)

def edit_produto(request, id):
    produto = Produto.objects.get(pk=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    
    else:
        form = ProdutoForm(instance=produto)

    contexto = {'form_prod': form, 'texto': 'Salvar'}
    return render(request, 'cadastro.html', contexto)

def del_produto(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('produtos')   

def cliente(request):
    lista_cliente = Cliente.objects.all()

    contexto = {

        'lista_cliente': lista_cliente
    }

    return render(request, 'cliente.html', contexto)

def cadastro_cliente(request):
    form_cliente = ClienteForm(request.POST or None)
    if form_cliente.is_valid():
        form_cliente.save()
        return redirect('index')
    contexto = {
        'form_cliente': form_cliente
    }

    return render(request, 'cadastro_cliente.html', contexto)


def del_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect('cliente')        

def edit_cliente(request, id):
    cliente = Cliente.objects.get(pk=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    
    else:
        form = ClienteForm(instance=cliente)

    contexto = {'form_cliente': form, 'texto': 'Salvar'}
    return render(request, 'cadastro_cliente.html', contexto)

def endereco(request):
    end_lista = Endereco.objects.all()

    contexto = {
        'end_lista': end_lista
    }

    return render(request, 'endereco.html', contexto)

def cadastro_endereco(request):
    form_endereco = EnderecoForm(request.POST or None)
    if form_endereco.is_valid():
        form_endereco.save()
        return redirect('endereco')
    contexto = {
        'form_endereco': form_endereco    
    }
        
    return render(request, 'cadastro_endereco.html', contexto)

def edit_endereco(request, id):
    endereco = Endereco.objects.get(pk=id)

    if request.method == 'POST':
        form = EnderecoForm(request.POST, instace=endereco)
        if form.is_valid():
            form.save()
            return redirect('endereco')
    else:
        form = EnderecoForm(instance=endereco)

    contexto = {'form_endereco': form, 'texto': 'Salvar'}
    return render(request, 'cadastro_endereco.html', contexto)  

def del_endereco(request, id):
    endereco = Endereco.objects.get(pk=id)
    endereco.delete()
    return redirect('endereco')      

    
def funcionario(request):
    lista_funcionario = Funcionario.objects.all()

    contexto = {
        'lista_funcionario': lista_funcionario
    }

    return render(request, 'funcionario.html', contexto)

def cadastro_funcionario(request):
    form_funcionario = FuncionarioForm(request.POST or None)
    if form_funcionario.is_valid():
        form_funcionario.save()
        return redirect('index')
    contexto = {
        'form_funcionario': form_funcionario
    }   

    return render(request, 'cadastro_funcionario.html', contexto) 

def edit_funcionario(request, id):
    funcionario = Funcionario.objects.get(pk=id)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario')
    else:
            form = FuncionarioForm(instance=funcionario)

            contexto = {
                'form_funcionario': form, 'texto': 'Salvar'
            }

    return render(request, 'cadastro_funcionario.html', contexto)

def del_funcionario(request, id):
    funcionario = Funcionario.objects.get(pk=id)
    funcionario.delete()

    return redirect('funcionario')  

def pedido(request):
    lista_pedido = Pedido.objects.all()

    contexto = {
        'lista_pedido': lista_pedido
    } 

    return render(request, 'pedido.html', contexto)

def cadastro_pedido(request):
    form_pedido = PedidoForm(request.POST or None)
    if form_pedido.is_valid():
        form_pedido.save()
        return redirect('pedido')
    contexto = {
        'form_pedido': form_pedido
    }   

    return render(request, 'cadastro_pedido.html', contexto) 

def edit_pedido(request, id):
    pedido = Pedido.objects.get(pk=id)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    else:
            form = PedidoForm(instance=pedido)

            contexto = {
                'form_pedido': form, 'texto': 'Salvar'
            }

    return render(request, 'cadastro_pedido.html', contexto) 

def del_pedido(request, id):
    pedido =  Pedido.objects.get(pk=id)
    pedido.delete()
    return redirect('pedido')
       
