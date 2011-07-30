from piston.handler import BaseHandler
from piston.utils import rc

from game.engine.models import *
from game.engine import utils


class PlayHandler(BaseHandler):
    allowed_method = ('POST',)
    
    def create(self,request):
        data = request.data
        user = request.user
        player = Character.objects.get(player=user)
        action = Action.objects.get(id=data.get('action_id'))
        
        utils.give_point(player,action)
        utils.give_reward(player,action)
        return rc.CREATED


class RewardHandler(BaseHandler):
    allowed_method = ('POST',)
    
    def create(self,request):
        data = request.data
        user = request.user
        player = Character.objects.get(player=user)
        action = Action.objects.get(id=data.get('action_id'))
        
        reward = Reward.objects.get(id=data.get('reward_id'))
        utils.reward_point(player,reward)
        return rc.CREATED


class LeaderBoardHandler(BaseHandler):
    allowed_method = ('POST',)
    fields = ('content', ('username','experience'),)
    def read(self,request):
        ch = Character.objects.all().order_by('experience')[0:11]
        d = {}
        d['content'] = [{'username':i.player.username,'experience':i.experience} for i in ch]
        return d
