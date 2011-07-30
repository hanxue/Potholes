from django.contrib import admin
from game.engine.models import Character
from game.engine.models import Action
from game.engine.models import Reward
from game.engine.models import RewardCondition


class CharacterAdmin(admin.ModelAdmin):
    pass


class ActionAdmin(admin.ModelAdmin):
    pass


class RewardAdmin(admin.ModelAdmin):
    pass


class RewardConditionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Character,CharacterAdmin)
admin.site.register(Action,ActionAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(RewardCondition,RewardConditionAdmin)
