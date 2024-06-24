from django.contrib import admin
from django.db import models
from .models import Receita, Categoria, Sugestao


admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(Sugestao)