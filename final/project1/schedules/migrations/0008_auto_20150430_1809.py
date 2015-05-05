# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0007_auto_20150414_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='meeting_assignment',
            field=models.ManyToManyField(to='schedules.MeetingAssignment', blank=True),
        ),
    ]
