# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.FileField(upload_to='http://api.aa-academyapp.org/resources'),
        ),
    ]
