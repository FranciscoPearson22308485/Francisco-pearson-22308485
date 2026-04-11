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

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField(blank=True)
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, blank=True)

    def __str__(self):
        return self.sigla

class Tecnologia(models.Model):
    CATEGORIA_CHOICES = [
        ('LG', 'Linguagem'),
        ('FW', 'Framework'),
        ('BD', 'Base de Dados'),
        ('FE', 'Ferramenta'),
        ('SO', 'Outro'),
    ]
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_oficial = models.URLField(blank=True)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES, default='LG')
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    url_github = models.URLField(blank=True)
    url_demo = models.URLField(blank=True)
    conceitos_uc = models.TextField(blank=True, help_text="Conceitos aplicados da UC")
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True, related_name='projetos')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=200)
    orientador = models.CharField(max_length=200, blank=True)
    ano = models.IntegerField()
    resumo = models.TextField(blank=True)
    url = models.URLField(blank=True)
    area = models.CharField(max_length=200, blank=True)
    destacado = models.BooleanField(default=False)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    NIVEL_CHOICES = [
        ('B', 'Básico'),
        ('I', 'Intermédio'),
        ('A', 'Avançado'),
    ]
    TIPO_CHOICES = [
        ('T', 'Técnica'),
        ('S', 'Soft Skill'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, default='B')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='T')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    TIPO_CHOICES = [
        ('CU', 'Curso'),
        ('CE', 'Certificação'),
        ('WO', 'Workshop'),
        ('AC', 'Académico'),
    ]
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_conclusao = models.DateField(blank=True, null=True)
    certificado = models.FileField(upload_to='certificados/', blank=True, null=True)
    url = models.URLField(blank=True)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='CU')
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.titulo

class Interesse(models.Model):
    CATEGORIA_CHOICES = [
        ('TEC', 'Tecnologia'),
        ('NEG', 'Negócio'),
        ('CIE', 'Ciência'),
        ('CUL', 'Cultura'),
        ('DES', 'Desporto'),
        ('OUT', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, default='TEC')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class MakingOf(models.Model):
    TIPO_CHOICES = [
        ('DER', 'Diagrama DER'),
        ('DEC', 'Decisão de Modelação'),
        ('ERR', 'Erro e Correção'),
        ('JUS', 'Justificação'),
        ('EVO', 'Evolução do Modelo'),
        ('IA',  'Uso de IA'),
    ]
    titulo               = models.CharField(max_length=200)
    data                 = models.DateField(auto_now_add=True)
    descricao            = models.TextField()
    foto                 = models.ImageField(upload_to='makingof/', blank=True, null=True)
    tipo                 = models.CharField(max_length=3, choices=TIPO_CHOICES, default='JUS')
    entidade_relacionada = models.CharField(
        max_length=100, blank=True,
        help_text="Nome genérico da entidade (ex: Tecnologia, TFC)"
    )
    uc      = models.ForeignKey(
        'UnidadeCurricular', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='makingof_entries'
    )
    projeto = models.ForeignKey(
        'Projeto', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='makingof_entries'
    )

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.get_tipo_display()} — {self.titulo}"