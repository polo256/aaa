# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mobile_App', '0016_sectordeskpost_sector_desk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectordeskpost',
            name='sector_desk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='secretariat.SectorDesk'),
        ),
    ]