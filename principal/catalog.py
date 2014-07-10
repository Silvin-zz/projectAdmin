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
from principal.models       import TargetType
from principal.models       import TaskType
from principal.models       import Projecttype
from business.ModelMapping  import ModelMapping


def catalogList(request):
    
    
    catalogname=request.GET["name"]
    
    if("targettype" in catalogname):
        objects = TargetType.objects()
    
    
    if("tasktype" in catalogname):
        objects = TaskType.objects()
    
    if("projecttype" in catalogname):
        objects = Projecttype.objects()
        
    
        
    mapping      = ModelMapping()
    return HttpResponse(json.dumps((mapping.catalogMapping(objects))), content_type="application/json")
    
    return HttpResponseRedirect("/")
    
 
 
 
def catalogRemove(request):
     catalogname=request.GET["name"]
     if("targettype" in catalogname):
         objectCatalog = TargetType.objects(pk=request.GET["id"]).get()
         
     if("tasktype" in catalogname):
         objectCatalog = TaskType.objects(pk=request.GET["id"]).get()
     if("projecttype" in catalogname):
         objectCatalog = Projecttype.objects(pk=request.GET["id"]).get()
     objectCatalog.delete();
     return HttpResponse();
     
     
def catalogSave(request):
     catalogname=request.GET["name"]
     if("targettype" in catalogname):
         objectCatalog = TargetType()
         
     if("tasktype" in catalogname):
         objectCatalog = TaskType()
     if("projecttype" in catalogname):
         objectCatalog = Projecttype()
     objectCatalog.name=request.GET["value"];
     objectCatalog.save();
     return HttpResponse();
     
    

def catalogNew(request):
    return render_to_response('catalog/new.html', {}, context_instance=RequestContext(request))
    