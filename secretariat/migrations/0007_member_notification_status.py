# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0006_auto_20170327_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='notification_status',
            field=models.BooleanField(default=1),
        ),
    ]
