# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0005_auto_20180616_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_pic',
            field=models.ImageField(default='Image', upload_to='p/'),
        ),
    ]
