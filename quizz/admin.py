from django.contrib import admin
from .models import Pergunta, Opcao

class OpcaoInline(admin.TabularInline):
    model = Opcao

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('texto',)
    search_fields = ('texto',)
    inlines = [OpcaoInline]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Opcao)
