# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_App', '0023_auto_20170319_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticecomment',
            name='attachment_type',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='name',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='status',
            field=models.IntegerField(default=1, editable=False),
        ),
    ]