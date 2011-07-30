from django.conf.urls.defaults import *
from game.issues.views import *


urlpatterns = patterns('',
    url('^submit',issue_submit,name="issue_submit"),
)
