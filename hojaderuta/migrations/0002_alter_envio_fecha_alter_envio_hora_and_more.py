# Generated by Django 5.1.2 on 2024-11-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojaderuta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='fecha',
            field=models.DateField(blank=True, default='27-11-2024', null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='envio',
            name='hora',
            field=models.TimeField(blank=True, default='00:03:45', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='fecha_de_modificacion',
            field=models.DateField(blank=True, default='2024-11-27', null=True),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='hora_de_modificacion',
            field=models.TimeField(blank=True, default='00:03:45', null=True, verbose_name='Hora de modificacion'),
        ),
    ]
