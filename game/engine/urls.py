from django.conf.urls.defaults import *
from game.engine.views import *


urlpatterns = patterns('',
    url('^experience/$',top_experience,name="top_experience"),
    url('^photographer/$',top_photographer,name="top_photographer"),
)
