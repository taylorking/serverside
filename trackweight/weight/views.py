from django.shortcuts import render
from django.views import generic
from weight.models import Weight
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone

class top_seven_view(generic.ListView):
  model = Weight
  context_object_name = 'latest_weight_list'
  template_name = 'weight/topseven.html'
  def get_queryset(self): 
    return Weight.objects.order_by('-date_recorded')[:7]
class create_weight_view(generic.edit.CreateView): 
  model = Weight
  fields = ['date_recorded','weight','measurement_confidence','comment'] 
# Create your views here.
