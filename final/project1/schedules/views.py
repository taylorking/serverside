from django.shortcuts import render
from django.views import generic
from schedules.models import Course, Room, Section, Instructor
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class instructor_create_view(generic.edit.CreateView):
    template_name = "schedules/instructor/create.html"
    model = Instructor
    fields =  ['title', 'email','name','preferences','requested_courses']

class instructor_view(generic.ListView):
    template_name = "schedules/instructor/index.html"
    model = Instructor
    context_object_name = 'instructor_list'
    fields =  ['title', 'email','name','preferences','requested_courses']
    def get_context_data(self, **kwargs):
        context = super(instructor_view, self).get_context_data(**kwargs)
        context['section_list'] = Section.objects.all()
        return context
    
class room_view(generic.ListView): 
    template_name = "schedules/room/index.html" 
    model = Room 
    context_object_name = 'latest_room_list'
    fields = ['building', 'building_abbreviation', 'room_number', 'capacity', 'course_type', 'comments'] 
#    def get_ontext_data(self, **kwargs):
 #     return Room.objects.order_by('room_number')

class course_view(generic.ListView):
    template_name='schedules/courses/index.html'
    context_object_name = 'latest_course_list'
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled','id']
    def get_queryset(self):
      return Course.objects.order_by('-title')

class course_detail_view(generic.DetailView):
    model = Course
    template_name='schedules/courses/detail.html'
    def get_context_data(self, **kwargs):
      context = super(course_detail_view, self).get_context_data(**kwargs)
      context['now'] = timezone.now()
      return context

class course_update_view(generic.edit.UpdateView):
    template_name='schedules/courses/create.html'
    model = Course
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled'] 
    @method_decorator(login_required(login_url='schedules:login'))
    def dispatch(self, *args, **kwargs): 
      return super(course_update_view, self).dispatch(*args, **kwargs)

class section_index_view(generic.ListView):
    template_name='schedules/sections/index.html'
    model = Section
    context_object_name = 'section_list'
    fields = ['course', 'section_number', 'instructor', 'meeting_assignment', 'type_room_needed','seats_required']

class course_create_view(generic.edit.CreateView):
    template_name='schedules/courses/create.html'
    model = Course 
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled'] 
    @method_decorator(login_required(login_url='schedules:login'))
    def dispatch(self, *args, **kwargs): 
      return super(course_update_view, self).dispatch(*args, **kwargs)

class course_delete_view(generic.edit.DeleteView):
    template_name='schedules/courses/delete.html'
    model = Course 
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled']
    @method_decorator(login_required(login_url='schedules:login'))
    def dispatch(self, *args, **kwargs): 
      return super(course_update_view, self).dispatch(*args, **kwargs)

class room_detail_view(generic.DetailView):
  template_name='schedules/room/detail.html' 
  model = Room 
# def get_queryset(self):
   ##     return schedules
# Create your views here.:
