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
    semester = models.CharField(max_length=4, choices=SEMESTERS)
    current = models.BooleanField()
    def __str__(self):
        return str(self.year) + ':' + self.semester
class Room(models.Model):
    building = models.CharField(max_length=200)
    building_abbreviation = models.CharField(max_length=4)
    room_number = models.CharField(max_length=4)
    capacity = models.IntegerField()
    day_times_available = models.DateTimeField(auto_now=False) 
    course_type = models.CharField(max_length=4,choices=COURSE_TYPES)
    comments = models.CharField(max_length=200)
    def __str__(self):
      return self.building_abbreviation + " " + self.room_number
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
    def __str__(self):
      return self.discipline + " " + str(self.course_number) + ": " + self.title 

class MeetingAssignment(models.Model):
    day = models.DateTimeField(auto_now=False)
    time = models.DateTimeField(auto_now=False)
    duration = models.FloatField()
    term = models.ForeignKey('Term')
    room = models.ForeignKey('Room')


class MeetingAssignmentField(models.Field):
    def __init(self):
        assign = MeetingAssignment()
        self.day = assign.day 
        self.time = assign.time
        self.duration = assign.duration
        self.term = assign.term
        self.room = assign.room
        super(MeetingAssignmentField, self).__init__()
    def db_type(self, connection): 
      return 'MeetingAssignment'

class Section(models.Model):
    term = models.ForeignKey('Term')
    course = models.ForeignKey('Course')
    instructor = models.ForeignKey('Instructor')
    section_number = models.IntegerField()
    meeting_assignment = MeetingAssignmentField()
 #   meeting_assignment = models.ManyToManyField('MeetingAssignment')
    type_room_needed = models.CharField(max_length=4,choices=COURSE_TYPES)
    seats_required = models.IntegerField()
    def __str__(self):
      return self.course + " " + self.meeting_assignment

class Instructor(models.Model):
    title = models.CharField(max_length = 200) 
    name = models.CharField(max_length=200)
    preferences = models.CharField(max_length=200)
    requested_courses = models.ManyToManyField('Course')
    def __str__(self):
      return self.name
    # Create your models here.
