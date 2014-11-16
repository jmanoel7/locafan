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
    url(r'^clientes/editar/$',     'clientes.views.editar',     name='clientes_editar'),
    url(r'^clientes/listar/$',     'clientes.views.listar',     name='clientes_listar'),
    url(r'^clientes/excluir/$',    'clientes.views.excluir',    name='clientes_excluir'),
    url(r'^fantasias/cadastrar/$', 'fantasias.views.cadastrar', name='fantasias_cadastrar'),
    url(r'^fantasias/editar/$',    'fantasias.views.editar',    name='fantasias_editar'),
    url(r'^fantasias/listar/$',    'fantasias.views.listar',    name='fantasias_listar'),
    url(r'^fantasias/excluir/$',   'fantasias.views.excluir',   name='fantasias_excluir'),
    url(r'^locacoes/cadastrar/$',  'locacoes.views.cadastrar',  name='locacoes_cadastrar'),
    url(r'^locacoes/editar/$',     'locacoes.views.editar',     name='locacoes_editar'),
    url(r'^locacoes/listar/$',     'locacoes.views.listar',     name='locacoes_listar'),
    url(r'^locacoes/excluir/$',    'locacoes.views.excluir',    name='locacoes_excluir'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += staticfiles_urlpatterns()
