# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0023_auto_20170318_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffactivity',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]