# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0023_auto_20170515_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='blog1',
            new_name='blog',
        ),
    ]