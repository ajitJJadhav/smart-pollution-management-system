# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-03 21:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollution_data', '0004_data_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 3, 2, 51, 391614)),
        ),
    ]