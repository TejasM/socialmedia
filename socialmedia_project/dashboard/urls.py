from dashboard import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login/$', views.login_user, name='login'),
                       url(r'^sign_up/$', views.sign_up, name='signup'),
                       url(r'^main/$', views.main, name='main'),
)