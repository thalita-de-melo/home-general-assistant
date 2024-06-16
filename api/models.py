from django.db import models

# Create your models here.

class Movies(models.Model):
    nome = models.CharField(max_length=100)
    pessoa = models.CharField(blank=False, max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    assistido = models.BooleanField(null=True)
    data_assistido = models.DateTimeField(null=True)
    # adicionar info da api the movie db ou adicionar 
    # a imagem do filme no volume do container

    def __str__(self):
        return self.nome
    
class Compras(models.Model):
    produto = models.CharField(max_length=100)
    pessoa = models.CharField(blank=False, max_length=30)
    categoria = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)
    comprado = models.BooleanField(null=True)
    data_comprado = models.DateTimeField(null=True)

    def __str__(self):
        return self.produto
