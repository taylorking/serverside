from django.contrib import admin
from schedules.models import Room, Course, Instructor, Section, Term 
# Register your models here.
admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Term)
