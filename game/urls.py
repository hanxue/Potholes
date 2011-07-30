from django.conf.urls.defaults import *
from commentor.views import leave_comment

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
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
=======
    (r'^blog/', include('example.urls')),
>>>>>>> e542a995053440b90a3ca817c848a1d14df7ad03
    (r'^accounts/', include('socialauth.urls')),
    (r'^admin/', admin.site.urls), 
    #(r'^$', leave_comment), 
    (r'^$', 'socialauth.views.signin_complete'),
    (r'^comments/post/', 'example_comments.views.post_comment'),
    (r'comments/', include('django.contrib.comments.urls')),
)

from django.conf import settings
if settings.DEBUG:
    
    urlpatterns += patterns('',
        # This is for the CSS and static files:
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
    
