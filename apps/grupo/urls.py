from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.grupo.views',
    url(r'^grupo/$', 'view_lista_grupos', name='vista_lista_grupos'),
    url(r'^grupo/(?P<id>.*)/editar/$', 'view_editar_grupo', name='vista_editar_grupo'),
    url(r'^grupo/add/$', 'view_add_grupo', name='vista_agregar_grupo'),
)
