from django.conf.urls import url
from django.shortcuts import render


# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json
from principal.models import User
from principal.models import Profile
from principal.models import Menu


## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models import Task

############### USER #######


def userList(request):
    users= User.objects()
    return render_to_response('user/list.html', {"users":users}, context_instance=RequestContext(request))

def userNew(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))


def userEdit(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))
    

def userSave(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))
    
    
############### PROFILE #######
    
def profileList(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))

def profileNew(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))


def profileEdit(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))
    

def profileSave(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))




############### MENU #######
    
def menuList(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))

def menuNew(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))


def menuEdit(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))
    

def menuSave(request):
    return render_to_response('user/list.html', {}, context_instance=RequestContext(request))





