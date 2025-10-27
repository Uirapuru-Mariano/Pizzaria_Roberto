from django import forms
from core.models import *

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