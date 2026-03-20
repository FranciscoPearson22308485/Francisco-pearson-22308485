from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='professor')

    def __str__(self):
        return self.nome
