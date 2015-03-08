from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from reglas import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Crons.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','reglas.views.listado'),
    url(r'^registrarCron/$','reglas.views.registrarCron'),
    url(r'^editarCron/(?P<codigo>\d+)/$','reglas.views.editarCrons'),
    url(r'^eliminarCron/(?P<codigo>\d+)/$','reglas.views.eliminarCron'),
    url(r'^eliCron/(?P<codigo>\d+)/$','reglas.views.eliCron')
)


