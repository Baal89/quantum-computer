# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-18 12:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200516_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]
