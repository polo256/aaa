# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0027_auto_20170318_1505'),
        ('mobile_app', '0004_auto_20170318_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorDeskPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post', models.TextField()),
                ('attachment', models.CharField(max_length=100)),
                ('attachment_type', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretariat.Member')),
                ('sector_desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mobile_App.SectorDesk')),
            ],
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='feedback',
        ),
    ]
