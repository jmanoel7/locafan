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
    url(r'^clientes/$',  'clientes.views.index',  name='clientes_index'),
    url(r'^fantasias/$', 'fantasias.views.index', name='fantasias_index'),
    url(r'^locacoes/$',  'locacoes.views.index',  name='locacoes_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += staticfiles_urlpatterns()
