# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-21 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_review'),
        ('reviews', '0002_auto_20200520_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
