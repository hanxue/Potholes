from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from game.issues.models import Issue
from django.core.context_processors import csrf
import game.engine.utils as game_utils
from game.engine.models import *
# Create your views here.

@login_required
def issue_submit(request):
    if request.method == 'POST': 
        player = Character.objects.get(player=user)
        if not player.action:
            return HttpResponseRedirect('/issues/view/'+str(id))
        form_data = request.POST
        title = form_data.get('title')
        description = form_data.get('description')
        location = form_data.get('location')
        user = request.user
        img = request.FILES.get('img')
        
        issue = Issue()
        issue.title = title
        issue.description = description
        issue.location = location
        issue.image = img
        issue.user = user
        issue.save()
        
        if location:
            action = Action.objects.get(id=3)
            game_utils.give_point(player,action)
            game_utils.give_reward(player,action)
        
        if img:
            action = Action.objects.get(id=2)
            game_utils.give_point(player,action)
            game_utils.give_reward(player,action)

        return HttpResponseRedirect('/issues/view/'+str(issue.id))
    else:
        return render_to_response('issue_submit.html',{},
              context_instance=RequestContext(request))

@login_required
def issue_list(request):
    issue = Issue.objects.all()
    return render_to_response('issue_list.html',{'issues':issue},
         context_instance=RequestContext(request))

@login_required
def issue_view(request,id):
    issue = Issue.objects.get(id=id)
    return render_to_response('issue_item.html',{'issue':issue},
         context_instance=RequestContext(request))

@login_required
def issue_upvote(request,id): 
    player = Character.objects.get(player=request.user)
    if not player.action:
        return HttpResponseRedirect('/issues/view/'+str(id))
    issue = Issue.objects.get(id=id)
    issue.upvote = issue.upvote + 1
    issue.save()
    action = Action.objects.get(id=1)
    game_utils.give_point(player,action)
    game_utils.give_point(player,action)
    return HttpResponseRedirect('/issues/view/'+str(id))

@login_required
def issue_downvote(request,id):
    player = Character.objects.get(player=request.user)
    if not player.action:
        return HttpResponseRedirect('/issues/view/'+str(id))

    issue = Issue.objects.get(id=id)
    issue.downvote = issue.downvote + 1
    issue.save()
    action = Action.objects.get(id=1)
    game_utils.give_point(player,action)
    game_utils.give_point(player,action)

    return HttpResponseRedirect('/issues/view/'+str(id))
