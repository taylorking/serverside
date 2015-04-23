from django.shortcuts import render
from django.views import generic
from schedules.models import Course, Room
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone
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

class course_create_view(generic.edit.CreateView):
    template_name='schedules/courses/create.html'
    model = Course 
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled'] 
    
class course_delete_view(generic.edit.DeleteView):
    template_name='schedules/courses/delete.html'
    model = Course 
    fields = ['discipline', 'course_number', 'course_type', 'title', 'description', 'hours_credit', 'contact_hours', 'sections_required', 'scheduling_controlled'] 
class room_detail_view(generic.DetailView):
  template_name='schedules/room/detail.html' 
  model = Room 
# def get_queryset(self):
   ##     return schedules
# Create your views here.
