# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0049_auto_20170320_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='company_logo',
            field=models.CharField(blank=True, default='logos/logogeneric.png', max_length=200, null=True),
        ),
    ]