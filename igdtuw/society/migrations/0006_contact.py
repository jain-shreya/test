# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0005_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_no', models.BigIntegerField()),
                ('fb', models.CharField(max_length=250)),
                ('twitter', models.CharField(max_length=250)),
                ('insta', models.CharField(max_length=250)),
                ('soc_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society.soclist')),
            ],
        ),
    ]
