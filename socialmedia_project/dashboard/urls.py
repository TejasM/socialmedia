from dashboard import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login/$', views.login_user, name='login'),
                       url(r'^sign_up/$', views.sign_up, name='signup'),
                       url(r'^main/$', views.main, name='main'),
                       url(r'^createSpec/$', views.create_spec, name='create_spec'),
                       url(r'^editSpec/(?P<spec_id>\d+)/$', views.edit_spec, name='edit_spec'),
)