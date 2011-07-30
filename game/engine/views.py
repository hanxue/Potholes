from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from game.engine.models import Character
from game.engine.models import ActionLog
import operator

def top_experience(request):
    ch = Character.objects.all().order_by('experience')[0:11]
    li = [{'username':i.player.username,'score':i.experience} for i in ch]
    return render_to_response('leaderboard.html',{'characters':li},
		context_instance = RequestContext(request))

def top_photographer(request):
    action_log = ActionLog.objects.filter(id=2)
    data = {}
    for i in action_log:
        if i.player.player.username in data:
            data[i.player.player.username] += 1
        else:
            data[i.player.player.username] = 1
    
    sorted_data = sorted(data.iteritems(),key=operator.itemgetter(1))
    print sorted_data
    ch = [{'username':i[0],'score':i[1]} for i in sorted_data]
    print ch
    return render_to_response('leaderboard.html',{'characters':ch},
		context_instance = RequestContext(request))

