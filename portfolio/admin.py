from django.contrib import admin
from .models import Licenciatura, Docente

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'instituicao', 'ano_inicio']
    search_fields = ['nome', 'sigla']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome']
