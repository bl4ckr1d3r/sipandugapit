# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-17 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapenduduk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapenduduk',
            name='status',
            field=models.CharField(choices=[('Belum Kawin', 'Belum Kawin'), ('Kawin', 'Kawin'), ('Janda', 'Janda'), ('Duda', 'Duda'), ('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')], default='Belum Kawin', max_length=100),
        ),
    ]
