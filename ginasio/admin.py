from django.contrib import admin
from .models import PT, Membro, Sessao

class SessaoAdmin(admin.ModelAdmin):
    list_display = ('membro', 'pt', 'data', 'hora')
    ordering = ('data', 'hora')
    search_fields = ('membro__nome', 'pt__nome')

admin.site.register(PT)
admin.site.register(Membro)
admin.site.register(Sessao, SessaoAdmin)
