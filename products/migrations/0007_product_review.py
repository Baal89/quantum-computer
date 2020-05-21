# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-21 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200520_1405'),
        ('products', '0006_auto_20200427_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Review'),
        ),
    ]
