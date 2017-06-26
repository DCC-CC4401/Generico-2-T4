# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 01:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_transacciones_nombrecomida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comida',
            name='idVendedor',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.AddField(
            model_name='comida',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comida',
            name='vendedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comida',
            name='nombre',
            field=models.CharField(default='Sin nombre', max_length=200),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='fecha',
            field=models.CharField(default='2017-06-26', max_length=200),
        ),
    ]
