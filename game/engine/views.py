from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from game.engine.models import Character

def top_experience(request):
    ch = Character.objects.all().order_by('experience')[0:11]
    return render_to_response('leaderboard.html',{'character':ch},
		context_instance = RequestContext(request))


