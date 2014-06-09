from django.conf.urls       import url
from django.shortcuts       import render

# Create your views here.
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from django.http            import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime               import datetime

import json
import time

from principal.models  		import Target
from principal.models  		import TargetType
from principal.models  		import TaskType
from principal.models  		import User
from principal.models  		import Project
from business.project       import BProject
from principal.models	 	import PriorityTask
from business.GApi	        import *



def targetList(request):

    bproject                    = BProject()
    users 						= User.objects()
    targettypes					= TargetType.objects()
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}


    return render_to_response('target/list.html', {
        "projects"      :   bproject.getAllProjects(True),
        "users"			:   users,
        "WNotify"       :   wNotify,
        "datestart"     :   time.strftime("%Y-%m-%d"),
        "dateend"       :   time.strftime("%Y-%m-%d"),
        "targettypes"	: 	targettypes,
    },context_instance = RequestContext(request))




def getTargetByProjectId(request):

	project      			= Project.objects(pk=request.POST["projectId"]).get()
	targets 				= Target.objects(project=project)

	return render_to_response('target/listByProject.html', {
        "targets"      :   targets,
    },context_instance 		= RequestContext(request))







def targetSave(request):


	target   				= Target()
	owner 					= User.objects(pk=request.POST["owner"])
	project 				= Project.objects(pk=request.POST["project"])
	targettype 				= TargetType.objects(pk=request.POST["targettype"])
	target.title 			= request.POST["title"]
	target.description 		= request.POST["description"]
	target.targettype 		= targettype[0]
	target.owner 			= owner[0]
	target.project 			= project[0]
	target.datestart 		= request.POST["datestart"]
	target.dateend 			= request.POST["dateend"]
	gapi                    = GApi()
	targetFolder            = gapi.createFolder("TG_" + request.POST["code"], project[0].folderreference)
	target.folderreference  = targetFolder["id"]
	target.code             = request.POST["code"]
    
	
	

	target.save()


	return render_to_response('target/resume.html', {
        "target"      :   target,
    },context_instance = RequestContext(request))




def targetDetail(request):
	
	users 						= User.objects()
	tasktypes					= TaskType.objects()
	priority 					= PriorityTask.objects()
	targetobject   				= Target.objects(pk=request.POST["targetid"])
	print(targetobject)
	return render_to_response('target/detail.html', {
        "target"      	:   targetobject[0],
        "users"			:	users,
        "tasktypes"		:	tasktypes,
        "priorities"	: 	priority,

    },context_instance = RequestContext(request))


def targetPrueba(request):
	return render_to_response('target/detail.html', {},context_instance = RequestContext(request))


