# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0021_remove_tag_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='blog',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='repository.Blog', verbose_name='所属博客'),
        ),
    ]