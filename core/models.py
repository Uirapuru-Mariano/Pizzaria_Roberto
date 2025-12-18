from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    Nome = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=15)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    logradouro = models.CharField(max_length=150)
    numero_da_casa = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.logradouro}, {self.numero_da_casa} - {self.bairro}"

class Situacao(models.Model):
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    data_pedido = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)
    obs = models.TextField(blank=True, null=True)
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    situacao_pedido = models.ForeignKey(Situacao, on_delete=models.PROTECT)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Pedido #{self.id} - Usuario {self.cliente.nome}"

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido {self.pedido.id})"
