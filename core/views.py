from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

def index(request):
    pizzas = Produto.objects.filter(id=1)
    lanches = Produto.objects.filter(id=2)
    bebidas = Produto.objects.filter(id=3)

    contexto = {
        'pizzas': pizzas,
        'lanches': lanches,
        'bebidas': bebidas
    }

    return render(request, 'index.html', contexto)

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('index')

def cadastro_user(request):
    form_user = UsuarioForm(request.POST or None)
    if form_user.is_valid():
        form_user.save()
        return redirect('login')
    
    contexto = {'form': form_user}
    return render(request, 'cadastro_user.html', contexto)

def produtos(request):
    lista_produto = Produto.objects.all()

    contexto = {

        'lista_produto': lista_produto
    }

    return render(request, 'produtos.html', contexto)

@login_required
def cadastro(request):
    form_prod = ProdutoForm(request.POST or None)
    if form_prod.is_valid():
        form_prod.save()
        return redirect('produtos')
    contexto = {
        'form_prod': form_prod, 'texto': 'Cadastrar'
    }

    return render(request, 'cadastro.html', contexto)

@login_required
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

@login_required
def del_produto(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('produtos')   

@login_required
def endereco(request):
    if request.user.is_superuser:
        end_lista = Endereco.objects.all()
    else:
        end_lista = Endereco.objects.filter(cliente_id=request.user.id)

    contexto = {
        'end_lista': end_lista
    }

    return render(request, 'endereco.html', contexto)

@login_required
def cadastro_endereco(request):
    form_endereco = EnderecoForm(request.POST or None)
    if form_endereco.is_valid():
        endereco = form_endereco.save(commit=False)
        endereco.cliente_id = request.user.id
        endereco.save()
        return redirect('endereco')
    contexto = {
        'form_endereco': form_endereco    
    }
        
    return render(request, 'cadastro_endereco.html', contexto)

@login_required
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

@login_required
def del_endereco(request, id):
    endereco = Endereco.objects.get(pk=id)
    endereco.delete()
    return redirect('endereco')      

@login_required
def pedido(request):
    if request.user.is_superuser:
        lista_pedido = Pedido.objects.all()
    else:
        lista_pedido = Pedido.objects.filter(cliente_id=request.user.id)

    contexto = {
        'lista_pedido': lista_pedido
    } 

    return render(request, 'pedido.html', contexto)

@login_required
def cadastro_pedido(request):
    form_pedido = PedidoForm(request.POST or None, user=request.user)
    if form_pedido.is_valid():
        wow = form_pedido.save(commit=False)
        wow.cliente_id = request.user.id
        wow.situacao_pedido_id = 1
        valor = Produto.objects.get(pk=wow.produto_id).valor
        wow.valor_total = valor * wow.quantidade
        wow.save()
        return redirect('pedido')
    
    contexto = {
        'form_pedido': form_pedido, 'texto': 'Cadastrar'}
    
    return render(request, 'cadastro_pedido.html', contexto)

@login_required
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

@login_required
def del_pedido(request, id):
    pedido =  Pedido.objects.get(pk=id)
    pedido.delete()
    return redirect('pedido')

@login_required   
def categoria(request):
    categoria = Categoria.objects.all()

    contexto = {
        'categoria': categoria

    }
    return render(request, 'categoria.html', contexto)