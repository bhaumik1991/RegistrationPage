# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, height_field='picture_height', max_length=255, null=True, upload_to='pictures/', width_field='picture_width'),
        ),
    ]
