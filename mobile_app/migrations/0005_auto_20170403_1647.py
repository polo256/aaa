# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0004_auto_20170403_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='mobile_app'),
        ),
        migrations.AlterField(
            model_name='sectordeskpost',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='mobile_app'),
        ),
    ]
