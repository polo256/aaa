# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_App', '0019_sectordeskpost_sector_desk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticecomment',
            name='attachment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sectordeskpost',
            name='attachment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sectordeskpostcomment',
            name='attachment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
