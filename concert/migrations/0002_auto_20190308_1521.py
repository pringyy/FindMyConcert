# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='giggoer',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarks', to='concert.Concert'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concert', to='concert.Venue'),
        ),
    ]