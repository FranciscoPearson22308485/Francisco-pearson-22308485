from django.contrib import admin
from .models import (Licenciatura, Docente, UnidadeCurricular, Tecnologia, 
                     Projeto, TFC, Competencia, Formacao, Interesse, MakingOf)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'instituicao', 'ano_inicio')
    search_fields = ('nome', 'sigla')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome',)

@admin.register(UnidadeCurricular)
class UCAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ano_curricular', 'semestre', 'ects')
    list_filter = ('ano_curricular', 'semestre', 'licenciatura')
    search_fields = ('nome', 'sigla')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    list_filter = ('categoria', 'nivel_interesse')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc', 'data_inicio')
    list_filter = ('uc',)
    search_fields = ('titulo', 'descricao')

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'destacado')
    list_filter = ('ano', 'area', 'destacado')
    search_fields = ('titulo', 'autor', 'orientador')

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    list_filter = ('tipo', 'nivel')
    search_fields = ('nome',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'tipo', 'data_inicio')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'instituicao')

@admin.register(Interesse)
class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'entidade_relacionada', 'data')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'entidade_relacionada')