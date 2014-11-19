from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.asistencia_alumno.views',
    url(r'^asistencia_alumno/$', 'view_lista_asistencia_alumnos', name='vista_lista_asistencia_alumnos'),
    url(r'^asistencia_alumno/(?P<id>.*)/editar/$', 'view_editar_asistencia_alumno', name='vista_editar_asistencia_alumno'),
    url(r'^asistencia_alumno/add/$', 'view_add_asistencia_alumno', name='vista_agregar_asistencia_alumno'),
    url(r'^asistencia_alumno/(?P<id>.*)/eliminar/$', 'view_eliminar_asistencia_alumno', name='vista_eliminar_asistencia_alumno'),
)
