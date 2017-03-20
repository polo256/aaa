# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 09:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secretariat', '0015_staffactivity_activity_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='my_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]