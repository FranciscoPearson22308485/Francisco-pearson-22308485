from django.contrib import admin
from .models import Licenciatura

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'instituicao', 'ano_inicio']
    search_fields = ['nome', 'sigla']
