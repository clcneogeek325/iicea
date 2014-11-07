from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.concepto_pago.views',
    url(r'^concepto_pago/$', 'view_lista_concepto_pagos', name='vista_lista_concepto_pagos'),
    url(r'^concepto_pago/(?P<id>.*)/editar/$', 'view_editar_concepto_pago', name='vista_editar_concepto_pago'),
    url(r'^concepto_pago/add/$', 'view_add_concepto_pago', name='vista_agregar_concepto_pago'),

)
