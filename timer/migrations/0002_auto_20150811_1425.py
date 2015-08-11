# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solve',
            old_name='cubetype',
            new_name='puzzle',
        ),
    ]
