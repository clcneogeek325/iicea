from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.perfil.views',
    url(r'^perfil/add/$', 'view_add_pefil', name='vista_agregar_perfil'),
    url(r'^perfil/$', 'view_lista_perfiles', name='vista_lista_perfiles'),
    url(r'^perfil/(?P<id>.*)/editar/$', 'view_editar_perfil', name='vista_editar_perfil'),

)
