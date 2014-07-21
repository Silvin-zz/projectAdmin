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


## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models       import DayByDayActivity
from principal.models       import DayByDay
from principal.models       import User
from business.ModelMapping  import ModelMapping
from business.GApi          import *
from principal.library      import Library


def List(request):
    
    activities = DayByDayActivity.objects()
    
    return render_to_response('calendar/list.html', { "activities": activities }, context_instance=RequestContext(request))
    
    
    
def Save(request):
    result = []
    
    
    
    if "new" in request.POST["action"]:
        event                   = DayByDay()
        activity                = DayByDayActivity.objects(pk=request.POST["activity"]).get()
        owner                   = User.objects(pk=request.session["userid"]).get()
        event.title             = request.POST["title"]
        event.description       = request.POST["description"]
        event.datestart         = request.POST["datestart"]
        event.dateend           = request.POST["dateend"]
        event.activity          = activity
        event.owner             = owner
        event.save()
        
        
    if("resize" in request.POST["action"]):
        print("entramos")
        event                   = DayByDay.objects(pk=request.POST["id"]).get()
        event.datestart         = request.POST["datestart"]
        event.dateend           = request.POST["dateend"]
        event.save()
        
        
    newevent                = DayByDay.objects(pk=event.id).get()
    mapping = ModelMapping()
    
    return HttpResponse(json.dumps(mapping.dayByDayMapping([newevent])), content_type="application/json")
    
    


def getAll(request):
    lb                      = Library()
    period                  = lb.getPeriodWeek()
    mapping                 = ModelMapping()
    owner                   = User.objects(pk=request.session["userid"]).get()
    if("datestart" in request.GET):
        period["start"]     = request.GET["datestart"]
        period["end"]       = request.GET["dateend"]
        
    activities              = DayByDay.objects(owner = owner, datestart__gte = period["start"], dateend__lte = period["end"])
    return HttpResponse(json.dumps(mapping.dayByDayMapping(activities)), content_type="application/json")
    
    
    
    
    
    
    
    
    

    