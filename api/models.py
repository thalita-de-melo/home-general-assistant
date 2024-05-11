from django.db import models

# Create your models here.

class Movies(models.Model):
    nome = models.CharField(max_length=100)
    pessoa = models.CharField(blank=False, max_length=30)
    assistido = models.BooleanField(null=True)
    # adicionar info da api the movie db ou adicionar 
    # a imagem do filme no volume do container

    def __str__(self):
        return self.nome
