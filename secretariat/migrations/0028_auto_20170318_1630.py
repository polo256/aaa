# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0027_auto_20170318_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='status',
            new_name='sub_status',
        ),
        migrations.AddField(
            model_name='member',
            name='company_logo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.TextField(default='This is my company description'),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='$2y$10$eM0VDmCiZq692kNgs4K5R.NFKFSQAkV0SkzAC7lW6Ib.iwy2LdvYu', max_length=200),
        ),
    ]
