# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_auto_20150430_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=200, default='cs@appstate.edu'),
        ),
    ]
