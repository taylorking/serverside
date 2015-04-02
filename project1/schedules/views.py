from django.shortcuts import render
from django.views import generic
class IndexView(generic.ListView):
    template_name='schedules/index.html'
    context_object_name = 'latest_course_list'

   # def get_queryset(self):
   ##     return schedules
# Create your views here.
