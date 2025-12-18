from django import forms
from core.models import *
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'Nome', 'Telefone', 'email', 'password1', 'password2']

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
        fields = ['produto', 'quantidade', 'obs', 'endereco_entrega','forma_pagamento']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PedidoForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['endereco_entrega'].queryset = Endereco.objects.filter(cliente_id=user)

#Em desuso
class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto','quantidade']                   