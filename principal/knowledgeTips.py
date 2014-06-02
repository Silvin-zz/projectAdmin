from django.conf.urls       import url
from django.shortcuts       import render

# Create your views here.
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from django.http            import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime               import datetime

import json


from principal.models       import KnowledgeTips
from principal.models       import Task
from principal.models       import User
from business.Auth          import googleAuth 
from django.conf            import settings

import time


def add(request):
    
    tip                 = KnowledgeTips()
    task                = Task.objects(pk=request.POST["taskId"]).get()
    tip.description     = request.POST["description"]
    tip.keywords        = request.POST["keywords"].split(",")
    tip.owner           = User.objects(pk=request.session["userid"]).get()
    tip.task            = task
    tip.save()
    return render_to_response('tips/show.html', {"tip": tip}, context_instance=RequestContext(request))
    
    
def listTips(request):
    task                = Task.objects(pk=request.POST["taskId"]).get()
    print("Llegando a la tarea :::::::::::::::")
    print(task)
    tips                = KnowledgeTips.objects(task=task)
    print("Llegando a los tips::::::::::::::::::::::::::::")
    print(tips)
    return render_to_response('tips/list.html', {"tips": tips}, context_instance=RequestContext(request))
    
    