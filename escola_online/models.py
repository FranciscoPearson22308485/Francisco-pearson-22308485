from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.numero})"

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos')

    def __str__(self):
        return self.nomev