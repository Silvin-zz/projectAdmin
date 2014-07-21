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
from principal.libExcel import libExcel


from principal.models       import Task
from principal.models       import Target
from principal.models       import User
from principal.models       import Project
from principal.models       import TaskType
from principal.models       import PriorityTask
from principal.models       import TimeLine
from principal.models       import DayByDayActivity
from principal.models       import DayByDay




import time
import datetime


def ListOwner(request):
    extra= ""
    if("owner" in request.GET):
       extra="?owner=true"
    return render_to_response('team/listowner.html', {"extra":extra}, context_instance=RequestContext(request))


def List(request):
    extra= ""
    if("owner" in request.GET):
       extra="?owner=true"
    return render_to_response('team/list.html', {"extra":extra}, context_instance=RequestContext(request))



def getResume(request):
    
    lb                      = Library()
    result                  = []
    if("owner" in request.GET):
       users 		    = User.objects(pk=request.session["userid"])
    else:
       users                   = User.objects()
    period                  = lb.getPeriodMonth()
    if("week"   in request.POST["type"]):
        period              = lb.getPeriodWeek()
    if("month"  in request.POST["type"]):
        period              = lb.getPeriodMonth()
        
    
    for user in users:
        
        tasks       = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"])
        projects    = Target.objects(tasks__in=tasks).distinct("project")
        print(projects)
        totaltasks  = len(tasks)
        finished    = Task.objects(owner=user, finished=True, datestart__gte= period["start"], datestart__lte= period["end"]).count()
        delayed     = Task.objects(owner=user, finished=False, dateend__lt  =datetime.datetime.now().date(), datestart__gte= period["start"], datestart__lte= period["end"]).count()
        intime      = Task.objects(owner=user, finished=False, dateend__gte =datetime.datetime.now().date(), datestart__gte= period["start"], datestart__lte= period["end"]).count()
        hours       = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("estimatedhours")
        hoursused   = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("usedhours")
        daytoday    = DayByDay.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("usedhours")
        percent     = 0
        if(totaltasks >0):
            percent = 100/totaltasks
        
        fpercent    = finished  *  percent
        fdelayed    = delayed   *  percent
        fintime     = intime    *  percent
        
        result.append({
            
            "tasks"             : totaltasks, 
            "finished"          : finished, 
            "delayed"           : delayed, 
            "intime"            : intime, 
            "assignedtime"      : hours, 
            "usedtime"          : hoursused ,
            "daytoday"          : daytoday,
            "projects"          : len(projects),
            "finishedpercent"   : "%.2f" % fpercent,
            "delayedpercent"    : "%.2f" % fdelayed,
            "intimepercent"     : "%.2f" % fintime,
            "owner"             : {
                                        "name"      : user.name,
                                        "img"       : "/static/images/users/" + str(user.getUrlImage()),
                                        "id"        : str(user.id)
                                  }
            })
    
    
    return HttpResponse(json.dumps(result), content_type="application/json")
        
        
        
    
        
