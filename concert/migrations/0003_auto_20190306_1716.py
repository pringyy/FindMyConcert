# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0002_auto_20190306_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='concert',
            old_name='startTime',
            new_name='start_time',
        ),
    ]
