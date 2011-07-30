from django.conf.urls.defaults import *
from game.issues.views import *


urlpatterns = patterns('',
    url('^submit/$',issue_submit,name="issue_submit"),
    url('^view/(?P<id>\d)+/$',issue_view,name="issue_view"),
    url('^list/',issue_list,name="issue_list"),
    url('upvote/(?P<id>\d+)/$',issue_upvote,name="issue_upvote"),
    url('downvote/(?P<id>\d+)/$',issue_downvote,name="issue_downvote"),
)
