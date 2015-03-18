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

from principal.models       import DayByDay
from principal.models       import DayByDayActivity
from principal.models       import Task
from principal.models       import Target
from principal.models       import User
from principal.models       import Project
from principal.models       import TaskType
from principal.models       import PriorityTask
from principal.models       import TimeLine
from principal.models       import DayByDayActivity
from principal.models       import DayByDay
from principal.models       import Area




import time
import datetime


def ListOwner(request):
    user                    = User.objects(pk=request.session["userid"]).get()
    if("owner" in request.GET):
       extra="?owner=true"
    return render_to_response('team/listowner.html', {"extra":extra, "area": user.area, "start": period["start"], "end": period["end"]}, context_instance=RequestContext(request))


def resumeOne(request):
    user                    = User.objects(pk=request.session["userid"]).get()
    areas                   = Area.objects()
    lb                      = Library()
    period                  = lb.getPeriodWeek()
    extra                   = ""
    return render_to_response('team/resumeone.html', { "areas":areas,  "extra":"sasasas", "area": user.area, "start": period["start"], "end": period["end"]}, context_instance=RequestContext(request))




def List(request):
    user                    = User.objects(pk=request.session["userid"]).get()
    extra= ""
    if("owner" in request.GET):
       extra="?owner=true"
    return render_to_response('team/list.html', {"extra":extra, "area": user.area}, context_instance=RequestContext(request))



def getResume(request):
    
    lb                      = Library()
    result                  = []
    user                    = User.objects(pk=request.session["userid"]).get()
    if("owner" in request.GET):
       users 		    = User.objects(pk=request.session["userid"])
    else:
       users                   = User.objects(area=user.area)
    period                  = lb.getPeriodMonth()
    if("week"   in request.POST["type"]):
        period              = lb.getPeriodWeek()
    if("month"  in request.POST["type"]):
        period              = lb.getPeriodMonth()
        
    
    typeActivities = DayByDayActivity.objects(name__ne="Vacaciones")

    for user in users:

        resumeObject = {}
        aux          = []
        usertotal    = 0
        for typeActivity in typeActivities:
            total       = DayByDay.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"], activity=typeActivity).sum("usedhours")
            usertotal   = usertotal + total
            aux.append({ "name": typeActivity.name, "value": total })
            # tasks       = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"])
            # projects    = Target.objects(tasks__in=tasks).distinct("project")
            # totaltasks  = len(tasks)
            # finished    = Task.objects(owner=user, finished=True, datestart__gte= period["start"], datestart__lte= period["end"]).count()
            # delayed     = Task.objects(owner=user, finished=False, dateend__lt  =datetime.datetime.now().date(), datestart__gte= period["start"], datestart__lte= period["end"]).count()
            # intime      = Task.objects(owner=user, finished=False, dateend__gte =datetime.datetime.now().date(), datestart__gte= period["start"], datestart__lte= period["end"]).count()
            # hours       = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("estimatedhours")
            # hoursused   = Task.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("usedhours")
            # daytoday    = DayByDay.objects(owner=user, datestart__gte= period["start"], datestart__lte= period["end"]).sum("usedhours")
            # percent     = 0
            # if(totaltasks >0):
            #     percent = 100/totaltasks
            
            # fpercent    = finished  *  percent
            # fdelayed    = delayed   *  percent
            # fintime     = intime    *  percent
        
        result.append(
            {
                "events": aux,
                "owner" : {
                                "name"      : user.name,
                                "img"       : "/static/images/users/" + str(user.getUrlImage()),
                                "id"        : str(user.id)
                          },
                "total" :  usertotal

            }
        )
    
    return HttpResponse(json.dumps(result), content_type="application/json")



def resumeOneList(request):
    startdate   = request.POST["datestart"]
    enddate     = request.POST["dateend"]
    area        = "todos";
    resume      = []
    if "todos" not in request.POST["area"]:
        area    = Area.objects(pk=request.POST["area"]).get() 

        users   = User.objects(area=area)

    if "todos" in area:
        datos = DayByDay.objects(datestart__gte= startdate, datestart__lte= enddate).order_by( 'owner', 'datestart')
    else:
        datos = DayByDay.objects(owner__in= users, datestart__gte= startdate, datestart__lte= enddate).order_by( 'owner', 'datestart')

    for dato in datos:
        resume.append({
             "activity"     : dato.activity.name,
             "title"        : dato.title,
             "description"  : dato.description,
             "date"         : str(dato.datestart),
             "duration"     : dato.usedhours,
             "owner"        : {
                                    "name"      : dato.owner.name,
                                    "img"       : "/static/images/users/" + str(dato.owner.getUrlImage()),
                                    "id"        : str(dato.owner.id)
                               }

            })
    return HttpResponse(json.dumps(resume), content_type="application/json")


def resumeTwo(request):
    user                    = User.objects(pk=request.session["userid"]).get()
    areas                   = Area.objects()
    lb                      = Library()
    period                  = lb.getPeriodWeek()
    extra                   = ""
    return render_to_response('team/resumetwo.html', { "areas":areas,  "extra":"", "area": user.area, "start": period["start"], "end": period["end"]}, context_instance=RequestContext(request))




def resumeTwoList(request):
    lb                      = Library()
    result                  = []
    typeActivities          = DayByDayActivity.objects()
    area                    = "todos";
    startdate               = request.POST["datestart"]
    enddate                 = request.POST["dateend"]
    resume                  = []
    
    if "todos" not in request.POST["area"]:
        area                = Area.objects(pk=request.POST["area"]).get() 
        users               = User.objects(area=area)
    else:
        users               = User.objects()

    for user in users:

        resumeObject        = {}
        aux                 = []
        usertotal           = 0

        for typeActivity in typeActivities:
            total       = DayByDay.objects(owner=user, datestart__gte= startdate, datestart__lte= enddate, activity=typeActivity).sum("usedhours")
            usertotal   = usertotal + total
            aux.append({ "name": typeActivity.name, "value": total })

        result.append(
            {
                "events": aux,
                "owner" : {
                                "name"      : user.name,
                                "img"       : "/static/images/users/" + str(user.getUrlImage()),
                                "id"        : str(user.id),
                                "area"      : user.area.name,
                                "profile"   : user.profile.name
                          },
                "total" :  usertotal

            }
        )
    
    return HttpResponse(json.dumps(result), content_type="application/json")



def resumeThree(request):
    user                    = User.objects(pk=request.session["userid"]).get()
    areas                   = Area.objects()
    lb                      = Library()
    period                  = lb.getPeriodWeek()
    extra                   = ""
    return render_to_response('team/resumethree.html', { "areas":areas,  "extra":"", "area": user.area, "start": period["start"], "end": period["end"]}, context_instance=RequestContext(request))




def resumeThreeList(request):
    lb                      = Library()
    result                  = []
    activityObject          = DayByDayActivity.objects(name="Proyecto").get();
    typeActivities          = Project.objects()
    area                    = "todos";
    startdate               = request.POST["datestart"]
    enddate                 = request.POST["dateend"]
    resume                  = []
    
    if "todos" not in request.POST["area"]:
        area                = Area.objects(pk=request.POST["area"]).get() 
        users               = User.objects(area=area)
    else:
        users               = User.objects()

    for user in users:

        resumeObject        = {}
        aux                 = []
        usertotal           = 0

        for typeActivity in typeActivities:
            total       = DayByDay.objects(owner=user, datestart__gte= startdate, datestart__lte= enddate, activity=activityObject, project=typeActivity).sum("usedhours")
            usertotal   = usertotal + total
            if total >0:
                aux.append({ "name": typeActivity.title, "value": total })

        if usertotal >0:
            
            result.append(
                {
                    "events": aux,
                    "owner" : {
                                    "name"      : user.name,
                                    "img"       : "/static/images/users/" + str(user.getUrlImage()),
                                    "id"        : str(user.id),
                                    "area"      : user.area.name,
                                    "profile"   : user.profile.name
                              },
                    "total" :  usertotal

                }
            )
        usertotal =0;
    
    return HttpResponse(json.dumps(result), content_type="application/json")

        
        
        
    
        
