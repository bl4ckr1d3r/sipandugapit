# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-17 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datapenduduk', '0002_auto_20211217_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomor', models.CharField(max_length=100)),
                ('tanda_tangan', models.CharField(choices=[('Kepala Desa', 'AMAN'), ('Sekertaris Desa', 'Muhammad Yakub')], default='Kepala Desa', max_length=100)),
                ('jenis', models.CharField(max_length=100)),
                ('jumlah', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('mulai', models.CharField(max_length=100)),
                ('jenis_sku', models.CharField(choices=[('SKU PETANI', 'SKU PETANI'), ('SKU TAMBAK', 'SKU TAMBAK'), ('SKU PETERNAK', 'SKU PETERNAK'), ('SKU KIOS', 'SKU KIOS')], default='SKU PETANI', max_length=100)),
                ('penduduk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datapenduduk.DataPenduduk')),
            ],
        ),
    ]
