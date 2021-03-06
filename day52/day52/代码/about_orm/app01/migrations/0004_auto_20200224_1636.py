# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-24 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20200224_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='app01.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='app01.Publisher'),
        ),
    ]
