# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-20 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_bug_debug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debug',
            name='bug',
        ),
        migrations.AddField(
            model_name='debug',
            name='bug_id',
            field=models.IntegerField(default=0),
        ),
    ]
