from django.contrib import admin
from polls.models import Question, Choice
#class QuestionAdmin(admin.ModelAdmin): 
   #  fields = ['pub_date', 'question_text'] 
   # fieldsets = [ 
   #         (None, {'fields':['question_text']}),
   #         ('Date Information', {'fields': ['pub_date']}), 
   #     ]
admin.site.register(Choice)
#admin.site.register(Question,QuestionAdmin)
# Register your models here.
