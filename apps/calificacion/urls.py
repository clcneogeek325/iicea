from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.calificacion.views',
    url(r'^calificacion/$', 'view_lista_calificacions', name='vista_lista_calificacions'),
    url(r'^calificacion/(?P<id>.*)/editar/$', 'view_editar_calificacion', name='vista_editar_calificacion'),
    url(r'^calificacion/add/$', 'view_agregar_calificacion', name='vista_agregar_calificacion'),
)
