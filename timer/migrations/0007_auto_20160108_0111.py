# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0006_auto_20160108_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solve',
            old_name='time',
            new_name='date',
        ),
    ]
