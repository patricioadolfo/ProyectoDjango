# Generated by Django 4.2 on 2025-01-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojaderuta', '0016_alter_envio_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='fecha',
            field=models.DateField(blank=True, default='2025-01-18', null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='envio',
            name='hora',
            field=models.TimeField(blank=True, default='14:24:29', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='fecha_de_modificacion',
            field=models.DateField(blank=True, default='2025-01-18', null=True),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='hora_de_modificacion',
            field=models.TimeField(blank=True, default='14:24:29', null=True, verbose_name='Hora de modificacion'),
        ),
    ]
