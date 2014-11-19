from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.pago.views',
    url(r'^pago/$', 'view_lista_pagos', name='vista_lista_pagos'),
    url(r'^pago/(?P<id>.*)/editar/$', 'view_editar_pago', name='vista_editar_pago'),
    url(r'^pago/(?P<id>.*)/eliminar/$', 'view_eliminar_pago', name='vista_eliminar_pago'),
    url(r'^pago/add/$', 'view_add_pago', name='vista_agregar_pago'),
)
