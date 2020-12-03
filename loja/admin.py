from django.contrib import admin
from loja.models import Produto, Venda, itensVenda


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'codigo_produto', 'descricao', 'valor', 'categoria', 'ativo')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 20


admin.site.register(Produto, Produtos)


class Vendas(admin.ModelAdmin):
    list_display = ('id', 'codigo_venda', 'valorTotal', 'valorPago', 'data_venda',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Venda, Vendas)


class itensVendas(admin.ModelAdmin):
    list_display = ('id','produto', 'quantidade', 'valorUnitario')
    list_display_links = ('id',)


admin.site.register(itensVenda, itensVendas)
