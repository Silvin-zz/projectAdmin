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


## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models import Task
from principal.models import Target
from principal.models import User
from principal.models import TaskType
from principal.models import PriorityTask
from principal.models import TimeLine
from business.GApi	  import *



import time


def taskList(request):
    
    taskObject                  = BTask();
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}
    
    return render_to_response('tasks/list.html', {"tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    
    
    
    
def taskAdd(request):
    taskObject  = BTask();
    return render_to_response('tasks/list.html', {"tasks":taskObject.getAll(True)}, context_instance=RequestContext(request))
    


    
def taskAdmin(request):
    return render_to_response('tasks/show2.html', {}, context_instance=RequestContext(request))




def myTasks(request):

    tasks   = Task.objects(owner=request.session["userid"], finished=False).order_by("-datestart", "priority__number")
    return render_to_response('task/assigned.html', {"tasks":tasks}, context_instance=RequestContext(request))




def showDetail(request):
    taskObject  = Task.objects(pk=request.POST["taskId"]).order_by('-timelinasdadasde__date').get()
    timelines   = taskObject.timeline
    return render_to_response('tasks/show.html', {"timelines": timelines, "task":taskObject}, context_instance=RequestContext(request))





def saveTimeLine(request):
    print("llegamos")
    tmObject                = TimeLine()
    tmObject.hoursspend     = request.POST["occupiedhours"]
    tmObject.activity       = request.POST["activity"]
    tmObject.endpercent     = request.POST["endpercent"]
    tmObject.urlreference1  = request.POST["reference1"]
    tmObject.urlreference2  = request.POST["reference2"]
    tmObject.owner          = User.objects(pk=request.session["userid"]).get()
    Task.objects(pk=request.POST["taskId"]).update_one(push__timeline=tmObject)

    taskObject              = Task.objects(pk=request.POST["taskId"]).get()
    taskObject.updateEndPercent(tmObject.endpercent)
    taskObject.updateHoursSpend(tmObject.hoursspend)
    timelines               = taskObject.timeline
    return render_to_response('task/showtimeline.html', {"timelines": timelines}, context_instance=RequestContext(request))



    
    
    
def taskSave(request):



    #targetObject                = 
    tasktypeObject              = TaskType.objects(pk=request.POST["tasktype"]).get()
    userObject                  = User.objects(pk=request.POST["owner"]).get()
    priorityObject              = PriorityTask.objects(pk=request.POST["priorityId"]).get()
    taskObject                  = Task()

    print("Prioridad")
    print(priorityObject.name)
    print(priorityObject.id)
    iscritical                  = False
    if("iscritical" in request.POST):
        iscritical = True

    target                      = Target.objects(pk=request.POST["targetId"]).get()
    taskObject.title            = request.POST["title"]
    taskObject.description      = request.POST["description"]
    taskObject.datestart        = request.POST["datestart"]
    taskObject.dateend          = request.POST["dateend"]
    taskObject.estimatedhours   = request.POST["estimatedhours"]
    taskObject.title            = request.POST["title"]
    taskObject.iscritical       = iscritical
    taskObject.tasktype         = tasktypeObject
    taskObject.owner            = userObject
    taskObject.priority         = priorityObject
    gapi                        = GApi()
    taskFolder                  = gapi.createFolder("TK_" +request.POST["code"], target.folderreference)
    taskObject.folderreference  = taskFolder["id"]
    print(taskFolder["id"])
    taskObject.save()
    
    Target.objects(pk=request.POST["targetId"]).update_one(push__tasks=taskObject)
    return render_to_response('task/intable.html', {"task": taskObject}, context_instance=RequestContext(request))



    # taskObject  = BTask();
    # if taskObject.saveProgress(request.POST) == True :
    #     message                     = "The Progress Task  has Saved Correctly"
    #     request.session["WNotify"]  = {"message": message, "type": "success", "title": "Update Data Task"}
    # else:
    #     message                     = "The Progress Task Do Not has been Saved"
    #     request.session["WNotify"]  = {"message": message, "type": "error", "title": "Update Data Task"}
    # return HttpResponseRedirect("list")
    