from django.contrib import admin
from .models import Festival, Artista

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'local', 'data_inicio', 'data_fim', 'preco_bilhete']
    list_filter = ['genero_musical']
    search_fields = ['nome', 'local']

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'genero', 'pais_origem']
    search_fields = ['nome']
