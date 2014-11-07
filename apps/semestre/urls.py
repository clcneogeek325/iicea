from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.semestre.views',
    url(r'^semestre/$', 'view_lista_semestres', name='vista_lista_semestres'),
    url(r'^semestre/(?P<id>.*)/editar/$', 'view_editar_semestre', name='vista_editar_semestre'),
    url(r'^semestre/add/$', 'view_add_semestre', name='vista_agregar_semestre'),

)
