from django.conf.urls import url
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json


from business.taskcomment import BTaskComment
from principal.models 		import Task
from principal.models       import Comment
from principal.models		import User


import time

def addForTask(request):
	commentObject   			= Comment()
	commentObject.owner			= User.objects(pk=request.session["userid"]).get()
	commentObject.description	= request.POST["comment"]

	Task.objects(pk=request.POST["taskId"]).update_one(push__comments=commentObject)
	return render_to_response('comments/show.html', {"comment": commentObject}, context_instance=RequestContext(request))
    

def listByTaskId(request):
    
    
    taskObject       = Task.objects(pk=request.POST["taskid"]).get()
    return render_to_response('comments/showall.html', {"comments": taskObject.comments}, context_instance=RequestContext(request))
     