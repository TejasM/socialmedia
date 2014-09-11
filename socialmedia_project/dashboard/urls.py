from dashboard import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^sample/$', views.sample, name='sample'),
)