# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cubetype', models.CharField(max_length=10)),
                ('scramble', models.CharField(max_length=50)),
                ('duration', models.DecimalField(decimal_places=3, max_digits=7)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
