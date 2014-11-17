from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.empleado.views',
    url(r'^empleado/$', 'view_lista_empleados', name='vista_lista_empleados'),
    url(r'^e/user_add/$', 'view_add_user', name='vista_agregar_usuario'),
    url(r'^empleado/(?P<id>.*)/editar/$', 'view_editar_empleado', name='vista_editar_empleado'),
	url(r'^empleado/(?P<id>.*)/eliminar/$', 'view_del_empleado', name='vista_eliminar_empleado'),
)
