from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    nome_pessoa = models.CharField(max_length=100)
    email = models.EmailField(default='sem_email@example.com')
    def __str__(self):
        return self.nome

class Sugestao(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    assunto_sugestao = models.CharField(max_length=50)
    sugestao = models.TextField()
    email = models.EmailField(default='sem_email@example.com')
    def __str__(self):
        return self.nome