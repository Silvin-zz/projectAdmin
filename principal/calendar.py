from django.conf.urls import url
from django.shortcuts import render




# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json
from business.task          import BTask
from business.user          import BUser
from principal.models       import AuthUser
from principal.library      import Library
from principal.libExcel     import libExcel
from business.calendarAPI   import calendarAPI


## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models       import DayByDayActivity
from principal.models       import Project
from principal.models       import DayByDay
from principal.models       import User
from business.ModelMapping  import ModelMapping
from business.GApi          import *
from business.calendarAPI   import *
from principal.library      import Library
import datetime

def List(request):
    
    calendar = calendarAPI()
    tmpusers = User.objects(email = request.session["email"])
    print("==================================================")
    print(len(tmpusers)) 
    tmpuser=tmpusers[0]
    print(tmpuser.initilizer) 
    if tmpuser.initilizer is None  or tmpuser.initilizer == False:
       return HttpResponseRedirect(calendar.getUrlAuthorization())
    calendar.getCredentialFromEmail(request.session["email"])
    calendar.listCalendarEvents()
    
    
    lb       = Library() 
    period = lb.getPeriodWeekToBack(2);
    
    activities = DayByDayActivity.objects()
    projects   = Project.objects()
    
    
    
    
    return render_to_response('calendar/list.html', { "activities": activities, "projects": projects, "startdate":period["start"].strftime('%Y/%m/%d') }, context_instance=RequestContext(request))
    
    
def Save(request):
    result = []
    
    
    if("remove" not in request.POST["action"]):
        
        if "new" in request.POST["action"]:
            event                   = DayByDay()
            activity                = DayByDayActivity.objects(pk=request.POST["activity"]).get()
            
            if(activity.name == "Proyecto"):
                project             = Project.objects(pk = request.POST["tmpproject"]).get()
                event.project       = project

            owner                   = User.objects(pk=request.session["userid"]).get()
            event.title             = request.POST["title"]
            event.description       = request.POST["description"]
            event.activity          = activity
            event.owner             = owner
            
            
            
        if("resize" in request.POST["action"]):
            
            event                   = DayByDay.objects(pk=request.POST["id"]).get()
            
        if("update" in request.POST["action"]):
            
            event                   = DayByDay.objects(pk=request.POST["id"]).get()
            activity                = DayByDayActivity.objects(pk=request.POST["activity"]).get()
            event.title             = request.POST["title"]
            event.description       = request.POST["description"]
            event.activity          = activity
            if(activity.name == "Proyecto"):
                project             = Project.objects(pk = request.POST["tmpproject"]).get()
                event.project       = project
            else:
                event.project       =  None
            
        event.datestart         = request.POST["datestart"]
        event.dateend           = request.POST["dateend"]
        event.save()
        
        mapping                 = ModelMapping()
        newevent                = DayByDay.objects(pk=event.id).get()
        newevent.calculateUsedTime()
        newevent.save()
        #if hasattr(event, 'isCalendar'):
            #if(event.isCalendar == True):
                #calendar = calendarAPI()
                #calendar.getCredentialFromEmail(request.session["email"])
                #calendar.updateEvent("primary", newevent.reference, newevent.title, newevent.description, newevent.datestart, newevent.dateend)
                
                
        result                  = mapping.dayByDayMapping([newevent])
    
    else:      #Eliminamos el evento completamente :D
        
        event                   = DayByDay.objects(pk=request.POST["id"]).get()
        #if hasattr(event, 'isCalendar'):
        #    if(event.isCalendar == True):
        #        calendar = calendarAPI()
        #        calendar.getCredentialFromEmail(request.session["email"])
        #        calendar.deleteEvent("primary", event.reference)
                
        event.delete()
        result                  = []
        
    
        
        
    
    
    return HttpResponse(json.dumps(result), content_type="application/json")
    
    


def getAll(request):
    lb                      = Library()
    period                  = lb.getPeriodWeek()
    mapping                 = ModelMapping()
    owner                   = User.objects(pk=request.session["userid"]).get()
    if("start" in request.GET):
        period["start"]     = datetime.datetime.fromtimestamp(int(request.GET["start"])).strftime('%Y-%m-%d %H:%M:%S')
        period["end"]       = datetime.datetime.fromtimestamp(int(request.GET["end"])).strftime('%Y-%m-%d %H:%M:%S')
        
        
    activities              = DayByDay.objects(owner = owner, datestart__gte = period["start"], dateend__lte = period["end"])
    return HttpResponse(json.dumps(mapping.dayByDayMapping(activities)), content_type="application/json")
    
    


def getSpendingHours(request):
    owner               = User.objects(pk=request.session["userid"]).get()
    period              = {"start":0, "end":0}
    period["start"]     = request.GET["start"]
    period["end"]       = request.GET["end"]
    hours               = DayByDay.objects(owner=owner, datestart__gte = period["start"], dateend__lte = period["end"]).sum("usedhours")
    result              = [{"totalhours": hours}]
    return HttpResponse(json.dumps(result), content_type="application/json")
    
    
    
    
    
    
    
    
    

    
