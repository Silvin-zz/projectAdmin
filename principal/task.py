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
    
    taskObject                  = BTask();
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}
    
    return render_to_response('tasks/list.html', {"tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    
    
    
    
def taskAdd(request):
    taskObject  = BTask();
    return render_to_response('tasks/list.html', {"tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    
    
    
    
def taskShow(request):
    taskObject = Task.objects.get(id=request.POST["taskid"])
    return render_to_response('tasks/show.html', {"task": taskObject}, context_instance=RequestContext(request))
    
    
    
    
    
def taskAdmin(request):
    return render_to_response('tasks/show2.html', {}, context_instance=RequestContext(request))
    
    
    
    
def taskSave(request):
    
    taskObject  = BTask();
    if taskObject.saveProgress(request.POST) == True :
        message                     = "The Progress Task  has Saved Correctly"
        request.session["WNotify"]  = {"message": message, "type": "success", "title": "Update Data Task"}
    else:
        message                     = "The Progress Task Do Not has been Saved"
        request.session["WNotify"]  = {"message": message, "type": "error", "title": "Update Data Task"}
    return HttpResponseRedirect("list")
    