# Generated by Django 5.1.2 on 2024-11-25 23:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estados', '0001_initial'),
        ('nodos', '0004_rename_nodos_destino_rename_otrosdestinos_nodo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='Ingrese una breve descripción del envío.', max_length=1000)),
                ('fecha', models.DateField(blank=True, default='25-11-2024', null=True, verbose_name='Fecha de Creacion')),
                ('hora', models.TimeField(blank=True, default='23:08:04', null=True, verbose_name='Hora de Creacion')),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destino', to='nodos.nodo')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estados.estado')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origen', to='nodos.nodo')),
                ('otro_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='otro_destino', to='nodos.destino')),
                ('otro_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='otro_origen', to='nodos.destino')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SeguimientoDeEnvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_modificacion', models.DateField(blank=True, default='2024-11-25', null=True)),
                ('hora_de_modificacion', models.TimeField(blank=True, default='23:08:04', null=True, verbose_name='Hora de modificacion')),
                ('envio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hojaderuta.envio')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estados.estado')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha_de_modificacion'],
            },
        ),
    ]