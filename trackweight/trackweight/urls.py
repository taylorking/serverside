from django.conf.urls import include, url
from django.contrib import admin
from weight import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'trackweight.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weight/add', views.create_weight_view.as_view(), name="create_weight"),
    url(r'^weight/', views.top_seven_view.as_view(), name="top_seven")
  
]
