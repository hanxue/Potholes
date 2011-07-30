from game.engine.models import Character
from game.engine.models import Action
from game.engine.models import ActionLog
from game.engine.models import Reward
from game.engine.models import RewardLog
from game.engine.models import RewardCondition

class Conditions:
    def __init__(self,condition,play_log):
        self.condition = condition
        self.play_log = play_log
        
    def get_reward(self):
        reward = getattr(self,self.condition.condition)()
        return reward
    
    def eq(self):
        if self.play_log.count() == self.condition.counter:
            return self.condition.reward
        return None

    def gt(self):
        if self.play_log.count() > self.condition.counter:
             return self.condition.reward
        return None
         
    def lt(self):
        if self.play_log.count() < self.condition.counter:
             return self.condition.reward
        return None
    
    def leq(self):
        if self.play_log.count() <= self.condition.counter:
             return self.condition.reward
        return None
    
    def geq(self):
        if self.play_log.count() >= self.condition.counter:
             return self.condition.reward
        return None

def give_point(player,action):
    print 'giving point'
    if player.action <= 0:
        return 
    player.action = player.action - action.action
    player.experience = player.experience + action.experience
    
    play_log = ActionLog(player=player,action=action)
    player.save()
    play_log.save()
    
def give_reward(player,action):
    print 'giving report'
    play_log = ActionLog.objects.filter(player=player,action=action)
    condition = RewardCondition.objects.filter(action=action)
    
    for i in condition:
        c = Conditions(i,play_log)
        if c.get_reward():
            reward = c.get_reward()
            check = RewardLog.objects.filter(player=player,reward=reward)
            if not check:
                reward_point(player,reward)

def reward_point(player,reward):
    orig_point = getattr(player,reward.attr)
    if not reward.inf:
        if reward.limit <= 0:
            return
    if reward.str_val:
        new_point = reward.str_val
    else:
        if reward.inc:
            new_point = orig_point + reward.point
        else:
            new_point = orig_point - reward.point
    
    setattr(player,reward.attr,new_point)
    print reward.attr 
    player.save()
    
    if not reward.inf:
        reward.limit = reward.limit - 1
        reward.save()
    reward_log = RewardLog(player=player,reward=reward)
    reward_log.save()
