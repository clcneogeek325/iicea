from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.home.views',
    url(r'^$', 'view_index', name='vista_principal'),
    url(r'^login/$', 'view_login', name='vista_loging'),
    url(r'^logout/$', 'view_logout', name='vista_logout'),
    url(r'^login_alumnos/$', 'view_login_alumnos', name='vista_login_alumnos'),
)
