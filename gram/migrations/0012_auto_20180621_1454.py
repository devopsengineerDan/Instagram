# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0011_auto_20180621_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-post_date',)},
        ),
    ]