# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0005_auto_20161002_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
