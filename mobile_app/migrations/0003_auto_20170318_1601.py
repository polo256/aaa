# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0002_auto_20170318_1559'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notices',
            new_name='Notice',
        ),
    ]
