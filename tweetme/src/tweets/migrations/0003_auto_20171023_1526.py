# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20171022_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=140),
        ),
    ]