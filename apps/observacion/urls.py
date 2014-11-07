from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.observacion.views',
    url(r'^observacion/$', 'view_lista_observaciones', name='vista_lista_observaciones'),
    url(r'^observacion/(?P<id>.*)/editar/$', 'view_editar_observacion', name='vista_editar_observacion'),
    url(r'^observacion/add/$', 'view_add_observacion', name='vista_agregar_observacion'),

)
