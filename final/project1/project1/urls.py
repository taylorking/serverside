from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^schedules/', include('schedules.urls', namespace='schedules')),
    url(r'^accounts/login/$' ,'django.contrib.auth.views.login')
 )
