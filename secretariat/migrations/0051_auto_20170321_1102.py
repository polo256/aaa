# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 08:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0050_auto_20170320_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffactivity',
            name='activity_end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
