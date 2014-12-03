from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iicia.views.home', name='home'),
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.pago.urls')),
    url(r'^', include('apps.nomina.urls')),
    url(r'^', include('apps.alumno.urls')),
    url(r'^', include('apps.asistencia_alumno.urls')),
    url(r'^', include('apps.asistencia_empleado.urls')),
    url(r'^', include('apps.empleado.urls')),
    url(r'^', include('apps.observacion.urls')),
    url(r'^', include('apps.concepto_pago.urls')),
    url(r'^', include('apps.horario.urls')),
    url(r'^', include('apps.tutor.urls')),
    url(r'^', include('apps.grupo.urls')),
    url(r'^', include('apps.semestre.urls')),
    url(r'^', include('apps.perfil.urls')),
    url(r'^', include('apps.materia.urls')),
    url(r'^', include('apps.calificacion.urls')),
    url(r'^', include('apps.chat.urls')),



    url(r'^admin/', include(admin.site.urls)),
) 
