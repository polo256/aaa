# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0040_auto_20170319_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='sector_desk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='secretariat.SectorDesk'),
        ),
    ]
