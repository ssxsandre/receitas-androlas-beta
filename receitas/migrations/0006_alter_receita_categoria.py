from django.db import migrations, models
import django.db.models.deletion

def set_default_categoria(apps, schema_editor):
    Receita = apps.get_model('receitas', 'Receita')
    Categoria = apps.get_model('receitas', 'Categoria')
    categoria_padrao, created = Categoria.objects.get_or_create(nome='Sem Categoria')
    Receita.objects.filter(categoria__isnull=True).update(categoria=categoria_padrao)

class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_receita_categoria_alter_receita_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.ForeignKey(default=None, null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, to='receitas.categoria'),
        ),
        migrations.RunPython(set_default_categoria, reverse_code=migrations.RunPython.noop),
    ]
