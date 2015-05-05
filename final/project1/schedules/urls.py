from django.conf.urls import patterns, url
from schedules import views
from django.contrib.auth import views as auth_views
urlpatterns = patterns('', 
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^course$', views.course_view.as_view(), name='course_index'),
    url(r'^course/create$', views.course_create_view.as_view(), name='course_create'),
    url(r'^course/detail/(?P<pk>\d+)$',views.course_detail_view.as_view(), name='course_detail'),
    url(r'^course/delete/(?P<pk>\d+)$',views.course_delete_view.as_view(), name='course_delete'),
    url(r'^course/update/(?P<pk>\d+)$',views.course_update_view.as_view(), name='course_update'), 
    url(r'^section/', views.section_index_view.as_view(), name="section_index"),
    url(r'^room', views.room_view.as_view(), name = "room_index"),  
    url(r'^instructor/$', views.instructor_view.as_view(), name="instructor_view"),

    url(r'^instructor/add', views.instructor_create_view.as_view(), name = "instructor_create" ) 
    #  url(r'^$(?P<pk>\d+)/$', views.DetailView.as_view(), name='tail'),

)
