from django.conf.urls import patterns, url
from schedules import views

urlpatterns = patterns('', 
    url(r'^course$', views.course_view.as_view(), name='course_index'),
    url(r'^course/create$', views.course_create_view.as_view(), name='course_create'),
    url(r'^course/detail/(?P<pk>\d+)$',views.course_detail_view.as_view(), name='course_detail'),
    url(r'^course/update/(?P<pk>\d+)',views.course_update_view.as_view(), name='course_update'), 
#  url(r'^$(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)
