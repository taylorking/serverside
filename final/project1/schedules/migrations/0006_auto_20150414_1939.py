# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_auto_20150409_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='day_times_available',
            field=models.CharField(max_length=200),
        ),
    ]
