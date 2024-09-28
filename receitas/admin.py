from django.contrib import admin
from .models import Receita, Categoria, Sugestao

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'email', 'nome_pessoa')
    search_fields = ('nome', 'ingredientes', 'modo_preparo',  'complemento_modo_preparo')
    list_filter = ('categoria',)
    fields = ('nome', 'ingredientes', 'modo_preparo',  'complemento_modo_preparo', 'categoria', 'email', 'nome_pessoa', 'imagem')

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Categoria)
admin.site.register(Sugestao)