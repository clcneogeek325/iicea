from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.home.views',
    url(r'^$', 'view_index', name='vista_principal'),

)
