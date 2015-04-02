# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('discipline', models.CharField(max_length=200)),
                ('course_number', models.IntegerField()),
                ('course_type', models.CharField(choices=[('LEC', 'Lecture'), ('LLEC', 'Large Lecture'), ('LAB', 'Lab'), ('OTR', 'Other')], max_length=4)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('hours_credit', models.IntegerField()),
                ('contact_hours', models.IntegerField()),
                ('sections_required', models.IntegerField()),
                ('scheduling_controlled', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='date_time_field',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('preferences', models.CharField(max_length=200)),
                ('requested_courses', models.ManyToManyField(to='schedules.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time', models.FloatField()),
                ('duration', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('building', models.CharField(max_length=200)),
                ('building_abbreviation', models.CharField(max_length=4)),
                ('room_number', models.CharField(max_length=4)),
                ('capacity', models.IntegerField()),
                ('course_type', models.CharField(choices=[('LEC', 'Lecture'), ('LLEC', 'Large Lecture'), ('LAB', 'Lab'), ('OTR', 'Other')], max_length=4)),
                ('comments', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('section_number', models.IntegerField()),
                ('type_room_needed', models.CharField(choices=[('LEC', 'Lecture'), ('LLEC', 'Large Lecture'), ('LAB', 'Lab'), ('OTR', 'Other')], max_length=4)),
                ('seats_required', models.IntegerField()),
                ('course', models.ForeignKey(to='schedules.Course')),
                ('instructor', models.ForeignKey(to='schedules.Instructor')),
                ('meeting_assignment', models.ManyToManyField(to='schedules.MeetingAssignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('year', models.IntegerField()),
                ('semster', models.CharField(choices=[('SPR', 'Spring'), ('SMR1', 'Summer1'), ('SMR2', 'Summer2'), ('SMR', 'Summer'), ('FAL', 'Fall')], max_length=4)),
                ('current', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='section',
            name='term',
            field=models.ForeignKey(to='schedules.Term'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meetingassignment',
            name='room',
            field=models.ForeignKey(to='schedules.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meetingassignment',
            name='term',
            field=models.ForeignKey(to='schedules.Term'),
            preserve_default=True,
        ),
    ]
