from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria')
    ordering = ('nome',)
    search_fields = ('nome',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'morada')
    ordering = ('nome',)
    search_fields = ('nome',)

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade')

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido)
admin.site.register(ItemPedido, ItemPedidoAdmin)
