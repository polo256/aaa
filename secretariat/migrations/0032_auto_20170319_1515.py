# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0031_remove_member_sector_desk'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='added_by',
            field=models.ForeignKey(default=729, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to='secretariat.Member'),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='secretariat.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='interest',
            field=models.ManyToManyField(blank=True, null=True, to='secretariat.MemberInterest'),
        ),
    ]