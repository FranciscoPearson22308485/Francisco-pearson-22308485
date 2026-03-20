from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='receitas')
    favoritos = models.ManyToManyField(User, related_name='receitas_favoritas', blank=True)

    def __str__(self):
        return self.nome
