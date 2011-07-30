from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from game.issues.models import Issue
# Create your views here.

@login_required
def issue_submit(request):
    if request.method == 'POST':
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
        issue.save()
        return HttpResponseRedirect('/')
    else:
        return render_to_response('issue_submit.html',{},
              context_instance=RequestContext(request))


@login_required
def issue_view(request,id):
    issue = Issue.objects.get(id=id)
    return render_to_respone('',{'issue':issue},
         context_instance=RequestContext(request))

@login_required
def issue_upvote(request,id):
    issue = Issue.objects.get(id=id)
    issue.upvote = issue.upvote + 1
    issue.save()
    return HttpResponseRedirect('/')

@login_required
def issue_upvote(request,id):
    issue = Issue.objects.get(id=id)
    issue.downvote = issue.downvote + 1
    issue.save()
    return HttpResponseRedirect('/')
