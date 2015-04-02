from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder

COURSE_TYPES = (        
    ('LEC', 'Lecture'),
    ('LLEC', 'Large Lecture'),
    ('LAB', 'Lab'),
    ('OTR', 'Other')
)
'''
class date_time_field(models.Field):
    description = "serialize time when the room is taken" 
    DAYS = (
            ('MON', 'Monday'),
            ('TUE', 'Tuesday'),
            ('WED', 'Wednesday'),
            ('THR', 'Thursday'),
            ('FRI', 'Friday')
        )
    day = models.CharField(max_length=3,choices=DAYS,default='MON')
    available = models.DateTimeField()
    def __init__(self):
        super(date_time_field, self).__init__()
    def serialize(self):
        return force_text(self)
    # I could do this so easily in node.js.. I have no idea how to do this in django
     # I googled it so this may or may not be correct
'''
class Term(models.Model): 
    year = models.IntegerField()
    SEMESTERS = ( 
            ('SPR', 'Spring'),
            ('SMR1', 'Summer1'),
            ('SMR2', 'Summer2'),
            ('SMR', 'Summer'),
            ('FAL', 'Fall')
    )
    semster = models.CharField(max_length=4, choices=SEMESTERS)
    current = models.BooleanField()

class Room(models.Model):
    building = models.CharField(max_length=200)
    building_abbreviation = models.CharField(max_length=4)
    room_number = models.CharField(max_length=4)
    capacity = models.IntegerField()
    day_times_available = models.DateTimeField(auto_now=True) 
    course_type = models.CharField(max_length=4,choices=COURSE_TYPES)
    comments = models.CharField(max_length=200)
#    available = JSONField(

class Course(models.Model):
    discipline = models.CharField(max_length=200)
    course_number = models.IntegerField()
    course_type = models.CharField(max_length=4,choices=COURSE_TYPES)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    hours_credit = models.IntegerField()
    contact_hours = models.IntegerField()
    sections_required = models.IntegerField() 
    scheduling_controlled = models.BooleanField()

class Section(models.Model):
    term = models.ForeignKey('Term')
    course = models.ForeignKey('Course')
    instructor = models.ForeignKey('Instructor')
    section_number = models.IntegerField()
    meeting_assignment = models.ManyToManyField('MeetingAssignment')
    type_room_needed = models.CharField(max_length=4,choices=COURSE_TYPES)
    seats_required = models.IntegerField()

class MeetingAssignment(models.Model):
    day = models.DateTimeField(auto_now=True)
    time = models.FloatField()
    duration = models.FloatField()
    term = models.ForeignKey('Term')
    room = models.ForeignKey('Room')


class Instructor(models.Model):
    title = models.CharField(max_length = 200) 
    name = models.CharField(max_length=200)
    preferences = models.CharField(max_length=200)
    requested_courses = models.ManyToManyField('Course')
    # Create your models here.
