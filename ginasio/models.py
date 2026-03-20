from django.db import models

class PT(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Membro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Sessao(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='sessoes')
    pt = models.ForeignKey(PT, on_delete=models.CASCADE, related_name='sessoes')
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ('pt', 'data', 'hora')
        verbose_name = 'Sessão'
        verbose_name_plural = 'Sessões'

    def __str__(self):
        return f"{self.membro} com {self.pt} em {self.data} às {self.hora}"
