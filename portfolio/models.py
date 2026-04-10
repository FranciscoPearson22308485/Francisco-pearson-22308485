from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    instituicao = models.CharField(max_length=200)
    ano_inicio = models.IntegerField()
    duracao_anos = models.IntegerField()
    url_pagina = models.URLField(blank=True)

    def __str__(self):
        return self.sigla
