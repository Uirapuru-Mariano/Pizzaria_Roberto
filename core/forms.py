from django import forms
from core.models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class DateInput(forms.DateInput):
    input_type:'date'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'valor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'senha']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cliente', 'logradouro', 'numero_da_casa', 'complemento',  'bairro', 'cep']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo', 'telefone', 'email', 'senha']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'atendente', 'valor_total', 'forma_pagamento', 'taxa_entrega', 'obs']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'pedido', 'quantidade']


                    