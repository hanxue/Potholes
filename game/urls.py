from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game.views.home', name='home'),
    # url(r'^game/', include('game.foo.urls')),
    (r'api/',include('game.api.urls')),
    (r'issues/',include('game.issues.urls')),
    #(r'^login/$', 'django.contrib.auth.views.login'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<Path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),    

    # Authentication files
    (r'^accounts/', include('socialauth.urls')),
    (r'^$', 'socialauth.views.signin_complete'),
)
