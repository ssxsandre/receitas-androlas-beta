# Generated by Django 3.2.23 on 2024-02-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=100)),
                ('assunto_sugestao', models.CharField(max_length=50)),
                ('sugestao', models.TextField()),
                ('email', models.EmailField(default='sem_email@example.com', max_length=254)),
            ],
        ),
    ]