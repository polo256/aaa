# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 23:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0011_auto_20170410_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='secretariat.Chapter', verbose_name='Select Country'),
        ),
    ]