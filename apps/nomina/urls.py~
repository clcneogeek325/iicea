from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.nomina.views',
    url(r'^nomina/$', 'view_lista_nominas', name='vista_lista_nominas'),
    url(r'^nomina/(?P<id>.*)/editar/$', 'view_editar_nomina', name='vista_editar_nomina'),
    url(r'^nomina/add/$', 'view_add_nomina', name='vista_agregar_nomina'),

)
