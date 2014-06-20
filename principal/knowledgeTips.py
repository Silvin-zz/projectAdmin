from django.conf.urls       import url
from django.shortcuts       import render

# Create your views here.
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from django.http            import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime               import datetime

import json


from principal.models       import KnowledgeTips
from principal.models       import Task
from principal.models       import User
from business.Auth          import googleAuth 
from django.conf            import settings
from mongoengine import Q

import time


def add(request):
    
    tip                 = KnowledgeTips()
    tip.reference       = request.POST["reference"]
    tip.referencetype   = request.POST["type"]
    tip.title           = request.POST["title"]
    tip.description     = request.POST["description"]
    keywords            = request.POST["keywords"].split(",")
    keywords            = [x.strip(' ') for x in keywords]
    tip.keywords        = keywords
    tip.owner           = User.objects(pk=request.session["userid"]).get()
    tip.save()
    return render_to_response('tips/show.html', {"tip": tip}, context_instance=RequestContext(request))
    
    
def listTips(request):
    tips                = KnowledgeTips.objects(reference=request.POST["reference"], referencetype="task")
    print("Llegando a los tips::::::::::::::::::::::::::::")
    print(tips)
    return render_to_response('tips/list.html', {"tips": tips}, context_instance=RequestContext(request))
    
    
def home(request):
    return render_to_response('tips/home.html', {}, context_instance=RequestContext(request))
    
def filterTips(request):
    
    vtKeywords        =request.POST["text"].split(" ")
    print(vtKeywords)
    tips2   = KnowledgeTips.objects(keywords__in=vtKeywords)
    print(tips2.to_json())
    tips    = KnowledgeTips.objects.filter((Q(title__icontains   =request.POST["text"])) | (Q(description__icontains   =request.POST["text"])) | (Q(keywords__in = vtKeywords ))  )
    return render_to_response('tips/filter.html', {"tips": tips }, context_instance=RequestContext(request))
    
    