# Generated by Django 4.2 on 2025-02-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojaderuta', '0019_alter_envio_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='hora',
            field=models.TimeField(blank=True, default='17:31:16', null=True, verbose_name='Hora de Creacion'),
        ),
        migrations.AlterField(
            model_name='seguimientodeenvio',
            name='hora_de_modificacion',
            field=models.TimeField(blank=True, default='17:31:16', null=True, verbose_name='Hora de modificacion'),
        ),
    ]
