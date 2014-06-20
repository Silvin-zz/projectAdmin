from django.conf.urls import url
from django.shortcuts import render



# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json
from business.task      import BTask
from business.user      import BUser
from principal.models   import AuthUser
from principal.library  import Library


## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models import Task
from principal.models import Target
from principal.models import User
from principal.models import TaskType
from principal.models import PriorityTask
from principal.models import TimeLine
from business.GApi	  import *



import time
import datetime


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

    
    return render_to_response('task/assigned.html', {}, context_instance=RequestContext(request))


def Tasksfilter(request):
    
    lb= Library()
    
    period  = {"start": datetime.datetime.now().date(), "end": datetime.datetime.now().date()}
    
    finished=False
    if("finished" in request.POST["finished"]):
        finished=True
    
    if("week" in request.POST["type"]):
        period  = lb.getPeriodWeek()
        
    if("month" in request.POST["type"]):
        period  = lb.getPeriodMonth()
        
    
    tasks   = Task.objects(owner=request.session["userid"], finished=finished, datestart__gte= period["start"], datestart__lte= period["end"]).order_by("-datestart", "priority__number")
    return render_to_response('task/listassigned.html', {"tasks":tasks}, context_instance=RequestContext(request))


def showDetail(request):
    taskObject  = Task.objects(pk=request.POST["taskId"]).order_by('-timeline').get()
    timelines   = list(reversed(taskObject.timeline))
    return render_to_response('tasks/show.html', {"timelines": timelines, "task":taskObject}, context_instance=RequestContext(request))







def saveTimeLine(request):

    tmObject                = TimeLine()
    tmObject.hoursspend     = float(request.POST["occupiedhours"])
    tmObject.activity       = request.POST["activity"]
    tmObject.endpercent     = request.POST["endpercent"]
    tmObject.urlreference1  = request.POST["reference1"]
    tmObject.urlreference2  = request.POST["reference2"]
    tmObject.owner          = User.objects(pk=request.session["userid"]).get()
    Task.objects(pk=request.POST["taskId"]).update_one(push__timeline=tmObject)

    taskObject              = Task.objects(pk=request.POST["taskId"]).get()
    
    taskObject.updateHoursSpend(tmObject.hoursspend)
    taskObject.updateEndPercent(tmObject.endpercent)
    
    
    timelines               = list(reversed(taskObject.timeline))
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
    
    print(request.POST)
    
    target                      = Target.objects(pk=request.POST["targetId"]).get()
    taskObject.title            = request.POST["title"]
    taskObject.description      = request.POST["description"]
    taskObject.datestart        = request.POST["datestart"]
    taskObject.dateend          = request.POST["dateend"]
    taskObject.estimatedhours   = float(request.POST["estimatedhours"])
    taskObject.title            = request.POST["title"]
    taskObject.code             = request.POST["code"]
    taskObject.iscritical       = iscritical
    taskObject.tasktype         = tasktypeObject
    taskObject.owner            = userObject
    taskObject.priority         = priorityObject
    gapi                        = GApi()
    taskFolder                  = gapi.createFolder("TK_" +request.POST["code"], target.folderreference)
    taskObject.folderreference  = taskFolder["id"]
    print("Nueva task")
    print(taskObject.to_json())
    taskObject.save()
    
    Target.objects(pk=request.POST["targetId"]).update_one(push__tasks=taskObject)
    return render_to_response('task/intable.html', {"task": taskObject}, context_instance=RequestContext(request))




def dashboard(request):
    period  = {"start": datetime.datetime.now().date(), "end": datetime.datetime.now().date()}
    tasks   = Task.objects(owner=request.session["userid"], finished=False, datestart__gte= period["start"], datestart__lte= period["end"]).order_by("-datestart", "priority__number")
    return render_to_response('task/dashboard.html', {"tasks":tasks}, context_instance=RequestContext(request))

    # taskObject  = BTask();
    # if taskObject.saveProgress(request.POST) == True :
    #     message                     = "The Progress Task  has Saved Correctly"
    #     request.session["WNotify"]  = {"message": message, "type": "success", "title": "Update Data Task"}
    # else:
    #     message                     = "The Progress Task Do Not has been Saved"
    #     request.session["WNotify"]  = {"message": message, "type": "error", "title": "Update Data Task"}
    # return HttpResponseRedirect("list")
    