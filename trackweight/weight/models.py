from django.db import models

class Weight(models.Model):
  date_recorded = models.DateTimeField(auto_now=False)
  weight = models.FloatField(default=0)
  confidence_choices = (('VC', 'Very Confident'), ('RC','Reasonably Confident'), ('NC', 'Not Confident'), ('G', 'Guess'))
  measurement_confidence = models.CharField(max_length=2, choices = confidence_choices)
  comment = models.CharField(max_length = 200, blank=True, null=True)

  def __str__(self): 
    return str(self.date_recorded) + " " + str(self.weight)

# Create your models here.
#
#   
