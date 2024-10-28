from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=45)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Moeda(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    qtd_moeda = models.FloatField()

    def __str__(self):
        return f'{self.usuario.username} | Moedas: {self.qtd_moeda}'

class Produto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=45)
    qtd_disponivel = models.IntegerField(default=0)
    preco = models.FloatField(default=0)
    descricao = models.CharField(max_length=100, default="")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    queridinho_da_galera = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra de {self.usuario} - {self.produto.nome}'