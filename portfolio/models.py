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

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_pagina_lusofona = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome
