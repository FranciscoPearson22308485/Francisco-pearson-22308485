from django.db import models

class Festival(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField(blank=True)
    genero_musical = models.CharField(max_length=100, blank=True)
    preco_bilhete = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Festival'
        verbose_name_plural = 'Festivais'
        ordering = ['data_inicio']

    def __str__(self):
        return self.nome


class Artista(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=100, blank=True)
    pais_origem = models.CharField(max_length=100, blank=True)
    festivais = models.ManyToManyField(Festival, blank=True, related_name='artistas')

    def __str__(self):
        return self.nome
