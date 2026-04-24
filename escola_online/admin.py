from django.contrib import admin
from .models import Curso, Professor, Aluno

# Registo simples para Professor e Aluno
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email') # Mostra estas colunas na lista
    search_fields = ('nome',)        # Permite pesquisar por nome

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero') # Mostra nome e número
    search_fields = ('nome', 'numero')

# Registo avançado para Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # O "molho" especial: cria uma interface de duas colunas 
    # para escolher alunos de forma muito mais rápida.
    filter_horizontal = ('alunos',) 
    
    list_display = ('nome', 'professor') # Mostra o curso e quem o leciona
    list_filter = ('professor',)         # Cria um filtro lateral por professor