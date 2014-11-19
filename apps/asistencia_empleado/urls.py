from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.asistencia_empleado.views',
    url(r'^asistencia_empleado/$', 'view_lista_asistencia_empleados', name='vista_lista_asistencia_empleados'),
    url(r'^asistencia_empleado/(?P<id>.*)/editar/$', 'view_editar_asistencia_empleado', name='vista_editar_asistencia_empleado'),
    url(r'^asistencia_empleado/add/$', 'view_add_asistencia_empleado', name='vista_agregar_asistencia_empleado'),
    url(r'^asistencia_empleado/(?P<id>.*)/eliminar/$', 'view_eliminar_asistencia_empleado', name='vista_eliminar_asistencia_empleado'),
)
