# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-12 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datapenduduk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataKartuKeluarga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nokk', models.CharField(max_length=16)),
                ('kecamatan', models.CharField(max_length=100)),
                ('kabupaten', models.CharField(max_length=100)),
                ('kodepos', models.CharField(max_length=100)),
                ('provinsi', models.CharField(max_length=100)),
                ('kepala_keluarga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datapenduduk.DataPenduduk')),
            ],
        ),
    ]