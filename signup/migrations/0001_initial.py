# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
            ],
        ),
    ]
