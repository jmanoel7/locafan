# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^locafan/', include('locafan.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'locafan.views.home', name='locafan_home'),
    url(r'^clientes/cadastrar/$',  'clientes.views.cadastrar',  name='clientes_cadastrar'),
    url(r'^clientes/buscar/$',     'clientes.views.buscar',     name='clientes_buscar'),
    url(r'^clientes/listar/$',     'clientes.views.listar',     name='clientes_listar'),
    url(r'^fantasias/cadastrar/$', 'fantasias.views.cadastrar', name='fantasias_cadastrar'),
    url(r'^fantasias/buscar/$',    'fantasias.views.buscar',    name='fantasias_buscar'),
    url(r'^fantasias/listar/$',    'fantasias.views.listar',    name='fantasias_listar'),
    url(r'^locacoes/cadastrar/$',  'locacoes.views.cadastrar',  name='locacoes_cadastrar'),
    url(r'^locacoes/buscar/$',     'locacoes.views.buscar',     name='locacoes_buscar'),
    url(r'^locacoes/listar/$',     'locacoes.views.listar',     name='locacoes_listar'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += staticfiles_urlpatterns()
