# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_recorded', models.DateTimeField()),
                ('weight', models.FloatField(default=0)),
                ('measurement_confidence', models.CharField(max_length=2, choices=[('VC', 'Very Confident'), ('RC', 'Reasonably Confident'), ('NC', 'Not Confident'), ('G', 'Guess')])),
                ('comment', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
