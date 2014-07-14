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



from principal.models       import Task
from principal.models       import Target
from principal.models       import User
from principal.models       import TaskType
from principal.models       import PriorityTask
from principal.models       import TimeLine
from business.ModelMapping  import ModelMapping
from business.GApi          import *


def List(request):
    
    return render_to_response('calendar/list.html', {}, context_instance=RequestContext(request))