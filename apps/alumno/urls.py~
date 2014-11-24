from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.alumno.views',
    url(r'^alumno/$', 'view_lista_alumnos', name='vista_lista_alumnos'),
    url(r'^alumno/(?P<id>.*)/editar/$', 'view_editar_alumno', name='vista_editar_alumno'),
    url(r'^user_add/$', 'view_add_user', name='vista_agregar_usuario_alumno'),
	url(r'^alumno/(?P<id>.*)/eliminar/$', 'view_del_alumno', name='vista_eliminar_alumno'),
)
