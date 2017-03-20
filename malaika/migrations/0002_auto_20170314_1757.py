# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('malaika', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=50)),
                ('children', models.ManyToManyField(to='malaika.Child')),
            ],
        ),
        migrations.AddField(
            model_name='child',
            name='child_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malaika.Parent', verbose_name='Parent'),
        ),
    ]