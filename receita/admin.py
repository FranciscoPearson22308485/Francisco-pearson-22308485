from django.contrib import admin
from .models import Ingrediente, Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Ingrediente)
admin.site.register(Receita, ReceitaAdmin)
