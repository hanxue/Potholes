from django.conf.urls.defaults import *
# from commentor.views import leave_comment
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game.views.home', name='home'),
    # url(r'^game/', include('game.foo.urls')),
    (r'api/',include('game.api.urls')),
    (r'issues/',include('game.issues.urls')),
    (r'top/',include('game.engine.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),    
)


