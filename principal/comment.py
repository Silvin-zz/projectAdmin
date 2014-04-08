from django.conf.urls import url
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json


from business.taskcomment import BTaskComment


import time

def add(request):
    commentObject   = BTaskComment();
    comment         = commentObject.addComment(request.session["userid"],request.POST["taskid"],request.POST["comment"]);
    return render_to_response('comments/show.html', {"menuOptions" :  json.loads(request.session["menu"]), "comment": comment}, context_instance=RequestContext(request))
    

def listByTaskId(request):
    
    commentObject  = BTaskComment();
    comments       = commentObject.getAll(request.POST["taskid"])
    return render_to_response('comments/showall.html', {"menuOptions" :  json.loads(request.session["menu"]), "comments": comments}, context_instance=RequestContext(request))
     