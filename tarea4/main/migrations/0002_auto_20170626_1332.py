# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='lat',
            field=models.FloatField(default=-33.457785),
        ),
        migrations.AddField(
            model_name='cliente',
            name='lng',
            field=models.FloatField(default=-70.663808),
        ),
    ]
