# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-27 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0007_cachetable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cachetable',
            options={'managed': False},
        ),
    ]
