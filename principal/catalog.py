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
from business.ModelMapping  import ModelMapping


def catalogList(request):
    
    
    catalogname=request.GET["name"]
    
    if("targettype" in catalogname):
        objects = TargetType.objects()
    
    
    if("tasktype" in catalogname):
        objects = TaskType.objects()
        
    
        
    mapping      = ModelMapping()
    return HttpResponse(json.dumps((mapping.catalogMapping(objects))), content_type="application/json")
    
    return HttpResponseRedirect("/")
    
    
    

def catalogNew(request):
    return render_to_response('catalog/new.html', {}, context_instance=RequestContext(request))
    