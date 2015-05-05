# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20150402_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='term',
            old_name='semster',
            new_name='semester',
        ),
    ]
