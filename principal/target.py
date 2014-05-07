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
from principal.models  		import User
from principal.models  		import Project
from business.project       import BProject



def targetList(request):

    bproject                    = BProject()
    users 						= User.objects()
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}


    return render_to_response('target/list.html', {
        "projects"      :   bproject.getAllProjects(True),
        "users"			:   users,
        "WNotify"       :   wNotify,
        "datestart"     :   time.strftime("%Y-%m-%d"),
        "dateend"       :   time.strftime("%Y-%m-%d"),
    },context_instance = RequestContext(request))




def getTargetByProjectId(request):

	project      	= Project.objects(pk=request.POST["projectId"]).get()
	targets 		= Target.objects(project=project)

	return render_to_response('target/listByProject.html', {
        "targets"      :   targets,
    },context_instance = RequestContext(request))




def targetSave(request):


	target   				= Target()
	owner 					= User.objects(pk=request.POST["owner"])
	project 				= Project.objects(pk=request.POST["project"])
	print(project)
	print(owner)


	target.title 			= request.POST["title"]
	target.description 		= request.POST["description"]
	target.owner 			= owner
	target.datestart 		= request.POST["datestart"]
	target.dateend 			= request.POST["dateend"]
	target.project 			= project
	target.save()

	project      	= Project.objects(pk=request.POST["projectId"]).get()
	targets 		= Target.objects(project=project)

	return render_to_response('target/resume.html', {
        "target"      :   target,
    },context_instance = RequestContext(request))













