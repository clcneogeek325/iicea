from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.calificacion.views',
    url(r'^calificacion/$', 'view_lista_calificacions', name='vista_lista_calificacions'),
    url(r'^calificacion/(?P<id>.*)/editar/$', 'view_editar_calificacion', name='vista_editar_calificacion'),
    url(r'^calificacion/(?P<id>.*)/eliminar/$', 'view_eliminar_calificacion', name='vista_eliminar_calificacion'),
    url(r'^calificacion/add/$', 'view_agregar_calificacion', name='vista_agregar_calificacion'),
    url(r'^lista_semestres/$', 'view_calificaciones_alumno', name='vista_calificaciones_alumno'),
     url(r'^calificacion/semestre/(?P<id_semestre>.*)/(?P<id_user>.*)/$', 'view_calificaciones_alumno_x_semestre', name='vista_cal_alumno_x_sem'),
)
