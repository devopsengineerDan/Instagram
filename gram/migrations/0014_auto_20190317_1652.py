# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-17 13:52
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0013_auto_20180621_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]