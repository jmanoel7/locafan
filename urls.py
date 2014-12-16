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
    url(
        r'^$',
        'home.views.index',
        name='home_index',
    ),
    url(
        r'^clientes/cadastrar/$',
        'clientes.views.cadastrar',
        name='clientes_cadastrar',
    ),
    url(
        r'^clientes/buscar_nome/$',
        'clientes.views.buscar_nome',
        name='clientes_buscar_nome',
    ),
    url(
        r'^clientes/buscar_cpf/$',
        'clientes.views.buscar_cpf',
        name='clientes_buscar_cpf',
    ),
    url(
        r'^clientes/editar/(?P<nome>.+)/$',
        'clientes.views.editar',
        name='clientes_editar',
    ),
    url(
        r'^clientes/listar/$',
        'clientes.views.listar',
        name='clientes_listar',
    ),
    url(
        r'^clientes/excluir/(?P<nome>.+)/$',
        'clientes.views.excluir',
        name='clientes_excluir',
    ),
    url(
        r'^fantasias/cadastrar/$',
        'fantasias.views.cadastrar',
        name='fantasias_cadastrar',
    ),
    url(
        r'^fantasias/editar/(?P<nome>.+)/(?P<tipo>[A-Z]{2})/(?P<tema>.+)/$',
        'fantasias.views.editar',
        name='fantasias_editar',
    ),
    url(
        r'^fantasias/buscar_nome/$',
        'fantasias.views.buscar_nome',
        name='fantasias_buscar_nome',
    ),
    url(
        r'^fantasias/buscar_tema/$',
        'fantasias.views.buscar_tema',
        name='fantasias_buscar_tema',
    ),
    url(
        r'^fantasias/buscar_tipo/$',
        'fantasias.views.buscar_tipo',
        name='fantasias_buscar_tipo',
    ),
    url(
        r'^fantasias/listar/$',
        'fantasias.views.listar',
        name='fantasias_listar',
    ),
    url(
        r'^fantasias/excluir/(?P<nome>.+)/(?P<tipo>[A-Z]{2})/(?P<tema>.+)/$',
        'fantasias.views.excluir',
        name='fantasias_excluir',
    ),
    url(
        r'^locacoes/cadastrar/$',
        'locacoes.views.cadastrar',
        name='locacoes_cadastrar',
    ),
    url(
        r'^locacoes/receber/(?P<id>\d+)/$',
        'locacoes.views.receber',
        name='locacoes_receber',
    ),
    url(
        r'^locacoes/listar/$',
        'locacoes.views.listar',
        name='locacoes_listar',
    ),
    url(
        r'^locacoes/excluir/(?P<id>\d+)/$',
        'locacoes.views.excluir',
        name='locacoes_excluir',
    ),
    url(
        r'^cep/',
        include('cep.urls'),
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += staticfiles_urlpatterns()
