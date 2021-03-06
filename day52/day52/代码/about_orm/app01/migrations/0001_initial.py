# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 00:55
from __future__ import unicode_literals

import app01.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='nick', max_length=32, null=True, unique=True, verbose_name='姓名')),
                ('age', models.IntegerField(default=18)),
                ('phone', app01.models.MyCharField(max_length=11, unique=True)),
                ('gender', models.BooleanField(choices=[(True, 'male'), (False, 'female')])),
                ('birth', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '所有用户信息',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Xx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=18)),
            ],
        ),
    ]
