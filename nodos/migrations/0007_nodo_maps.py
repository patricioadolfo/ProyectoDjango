# Generated by Django 4.2 on 2024-12-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodos', '0006_destino_mapa_nodo_mapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodo',
            name='maps',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
