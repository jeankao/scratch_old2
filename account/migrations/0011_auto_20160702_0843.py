# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-02 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_profile_lesson_event_open'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='lesson_event_open',
            new_name='video_event_open',
        ),
    ]
