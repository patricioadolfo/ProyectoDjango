# Generated by Django 4.2 on 2024-12-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojaderuta', '0015_alter_envio_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='hora',
            field=models.TimeField(blank=True, default='13:35:27', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='hora_de_modificacion',
            field=models.TimeField(blank=True, default='13:35:27', null=True, verbose_name='Hora de modificacion'),
        ),
    ]
