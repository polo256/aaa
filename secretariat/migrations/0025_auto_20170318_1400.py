# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0024_auto_20170318_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.BooleanField(),
        ),
    ]
