# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': (('view_categories', 'Can view current menu (categories)'),)},
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Category'),
            preserve_default=False,
        ),
    ]
