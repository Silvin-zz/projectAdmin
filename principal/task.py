from django.conf.urls import url
from django.shortcuts import render


# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json

from business.task import BTask
from business.user import BUser
from principal.models import AuthUser
from principal.models import Task

import time


def taskList(request):
    taskObject  = BTask();
    return render_to_response('tasks/list.html', {"menuOptions" :  json.loads(request.session["menu"]), "tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    
def taskAdd(request):
    taskObject  = BTask();
    return render_to_response('tasks/list.html', {"menuOptions" :  json.loads(request.session["menu"]), "tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    
def taskShow(request):
    taskObject = Task.objects.get(id=request.POST["taskid"])
    
    return render_to_response('tasks/show.html', {"menuOptions" :  json.loads(request.session["menu"]), "task": taskObject}, context_instance=RequestContext(request))