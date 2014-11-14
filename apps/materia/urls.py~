from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.horario.views',
    url(r'^horario/$', 'view_lista_horarios', name='vista_lista_horarios'),
    url(r'^horario/(?P<id>.*)/editar/$', 'view_editar_horario', name='vista_editar_horario'),
    url(r'^horario/add/$', 'view_add_horario', name='vista_agregar_horario'),

)
