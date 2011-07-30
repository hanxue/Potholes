from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from game.api.handler import PlayHandler
from game.api.handler import RewardHandler
from game.api.handler import LeaderBoardHandler
from piston.authentication import HttpBasicAuthentication


auth = HttpBasicAuthentication(realm='game')
ad = {'authentication':auth}

play_resource = Resource(handler=PlayHandler,**ad)
reward_resource = Resource(handler=RewardHandler,**ad)
leaderboard_resource = Resource(handler=LeaderBoardHandler,**ad)

urlpatterns = patterns('',
    url(r'game/$',play_resource),
    url(r'reward/$',reward_resource),
    url(r'leaderboard/$',leaderboard_resource),
)


