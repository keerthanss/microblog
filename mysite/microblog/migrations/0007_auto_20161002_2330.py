# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0006_auto_20161002_2303'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follows',
            unique_together=set([('follower', 'following')]),
        ),
    ]