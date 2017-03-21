# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretariat', '0029_member_status'),
        ('Mobile_App', '0007_noticecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('token', models.TextField()),
                ('notification_status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretariat.Member')),
            ],
        ),
    ]