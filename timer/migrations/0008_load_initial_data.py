# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 04:52
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='timer')

class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0007_auto_20160108_0111'),
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]