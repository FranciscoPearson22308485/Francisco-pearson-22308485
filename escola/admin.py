from django.contrib import admin
from .models import Turma, Aluno, Professor

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')
    ordering = ('nome',)
    search_fields = ('nome',)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma')
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
