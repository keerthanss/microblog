# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 06:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0012_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='privacy',
            field=models.CharField(choices=[('PB', 'Public'), ('PR', 'Private')], default='PB', max_length=2),
        ),
        migrations.AddField(
            model_name='shares',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microblog.Post'),
        ),
        migrations.AddField(
            model_name='shares',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microblog.User'),
        ),
    ]