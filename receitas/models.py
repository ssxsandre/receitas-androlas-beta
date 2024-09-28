from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    complemento_modo_preparo = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    nome_pessoa = models.CharField(max_length=50, blank=True, null=True)
    imagem = models.TextField()

    def __str__(self):
        return self.nome
class Sugestao(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    assunto_sugestao = models.CharField(max_length=50)
    sugestao = models.TextField()
    email = models.EmailField(default='sem_email@example.com')

    def __str__(self):
        return self.nome_pessoa