from django import forms
from core.models import *

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'valor']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero_da_casa', 'complemento',  'bairro', 'cep']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['valor_total', 'forma_pagamento', 'taxa_entrega', 'obs']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'pedido', 'quantidade']


                    