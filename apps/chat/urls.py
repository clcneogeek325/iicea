from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^chat/$', views.home, name='vista_chat'),
)
