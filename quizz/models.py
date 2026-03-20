from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.texto

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='opcoes')
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'

    def __str__(self):
        return self.texto
