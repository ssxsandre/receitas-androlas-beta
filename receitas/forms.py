from django import forms
from .models import Receita, Sugestao

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'modo_preparo', 'nome_pessoa', 'email']

class SugestaoForm(forms.ModelForm):
    class Meta:
        model = Sugestao
        fields = ['nome_pessoa', 'assunto_sugestao', 'sugestao', 'email']
