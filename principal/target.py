from django.conf.urls       import url
from django.shortcuts       import render

# Create your views here.
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from django.http            import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime               import datetime

import json
import time
import datetime
from principal.models       import Target
from principal.models       import TargetType
from principal.models       import TaskType
from principal.models       import User
from principal.models       import Project
from business.project       import BProject
from principal.models       import PriorityTask
from business.GApi          import *
from principal.library      import Library
from business.ModelMapping  import ModelMapping



def targetList(request):

    bproject                    = BProject()
    users                       = User.objects()
    targettypes                 = TargetType.objects()
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}
    owner                       = User.objects(pk=request.session["userid"]).get()
    
    return render_to_response('target/list.html', {
        
        "projects"      :   Project.objects.filter(active =True,owner=owner),
        "users"         :   users,
        "WNotify"       :   wNotify,
        "datestart"     :   time.strftime("%Y-%m-%d"),
        "dateend"       :   time.strftime("%Y-%m-%d"),
        "targettypes"   :   targettypes,
        
    },context_instance = RequestContext(request))




def getTargetByProjectId(request):
    print("Entramos :S:S:S:S:S")
    print(request.POST)
    project                 = Project.objects(pk=request.POST["projectId"]).get()
    lb                      = Library()
    period                  = {"start": datetime.datetime.now().date(), "end": datetime.datetime.now().date()}
    finished                = False

    if("finished"   in request.POST["finished"]):
        finished            = True
    if("week"       in request.POST["type"]):
        period              = lb.getPeriodWeek()
    if("month"      in request.POST["type"]):
        period              = lb.getPeriodMonth()
    if("pending"    in request.POST["type"]):
        
        finished            = False
        period["start"]     = datetime.date(1943,3, 13)
        targets             = Target.objects(project=project, finished=finished, datestart__gte= period["start"], dateend__lte= period["end"])
    else:
        if("all"    in request.POST["type"]):
            targets         = Target.objects(project=project, finished=finished)
        else:
            targets         = Target.objects(project=project, finished=finished, datestart__gte= period["start"], datestart__lte= period["end"])
    mapping                 = ModelMapping()
    return HttpResponse(json.dumps((mapping.targetMapping(targets))), content_type="application/json")







def targetSave(request):

    print(request.POST);

    if(len(request.POST["id"]) ==0 ):
	totaltargets		= str(Target.objects().count())
        gapi                    = GApi()
        target                  = Target()
        project                 = Project.objects(pk=request.POST["project"]).get()
        targetFolder            = gapi.createFolder("TG_" + totaltargets  +  "_" + request.POST["code"], project.folderreference)
        target.folderreference  = targetFolder["id"]
        target.project          = project

    else:
        target                  = Target.objects(pk=request.POST["id"]).get()


    mapping                     = ModelMapping() 
    owner                       = User.objects(pk=request.POST["owner"]).get()
    targettype                  = TargetType.objects(pk=request.POST["targettype"]).get()
    target.title                = request.POST["title"]
    target.description          = request.POST["description"]
    target.targettype           = targettype
    target.owner                = owner
    target.datestart            = request.POST["datestart"]
    target.dateend              = request.POST["dateend"]
    target.code                 = request.POST["code"]
    target.save()
    id                          = target.id
    target=Target.objects(pk=id).get()
    return HttpResponse(json.dumps((mapping.targetMapping([target]))), content_type="application/json")



def targetDetail (request):
    
    users                       = User.objects()
    tasktypes                   = TaskType.objects()
    priority                    = PriorityTask.objects()
    targetobject                = Target.objects(pk=request.POST["targetid"])
    print(targetobject)
    return render_to_response('target/detail.html', {
        "target"        :   targetobject[0],
        "users"         :   users,
        "tasktypes"     :   tasktypes,
        "priorities"    :   priority,

    },context_instance = RequestContext(request))


def targetPrueba(request):
    return render_to_response('target/detail.html', {},context_instance = RequestContext(request))


def targetRemove(request):

    if(request.method =="POST"):
        print("Este es el target IDD")
        print(request.POST["targetid"])
        target=Target.objects(pk=request.POST["targetid"]).get()
        target.delete()
    return HttpResponse()


def targetGetData(request):
    if(request.method=="POST"):
        target     =Target.objects(pk=request.POST["targetid"]).get()
        mapping    = ModelMapping()
        return HttpResponse(json.dumps((mapping.targetMapping([target]))), content_type="application/json")

def targetFinish(request):
    target              =Target.objects(pk=request.POST["targetid"]).get()
    target.finished     =True
    target.finishdate   =time.strftime("%Y-%m-%d")
    target.save()
    return HttpResponse()



