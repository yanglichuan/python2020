# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-10 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20200310_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointdetail',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
