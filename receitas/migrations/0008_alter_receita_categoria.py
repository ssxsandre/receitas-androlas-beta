# Generated by Django 4.0.6 on 2024-06-16 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0007_alter_receita_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.ForeignKey(blank=True, default='0', on_delete=django.db.models.deletion.CASCADE, to='receitas.categoria'),
        ),
    ]