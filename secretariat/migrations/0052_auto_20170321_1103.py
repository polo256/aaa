# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0051_auto_20170321_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffactivity',
            name='activity_end',
            field=models.DateTimeField(),
        ),
    ]
