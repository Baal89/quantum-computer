# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-28 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20200528_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
