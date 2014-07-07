from django.conf.urls import url
from django.shortcuts import render


# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

##Opciones para login y manejo de session.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers

##BUsiness
#from business.menu import BMenu
from principal.models import User
from principal.models import Menu
from principal.models import Projecttype
from principal.models import TargetType
from principal.models import TaskType
from principal.models import PriorityTask
from principal.models import driveConfiguration
from principal.models import Menu
from principal.models import Profile
from bson           import json_util
import json
import urllib2

import httplib2








def userList(request):

    titulo = ""
    return render_to_response('userList.html',{'title' :titulo})


#Login de Usuario


def home (request):
    
    
    
    print("llegamos")
    if(request.method=="POST"):
        print("Entramos al post")
        
        print(request.POST)
        
        users   =   User.objects(username=request.POST["username"], password=request.POST["password"])
        print(users)
        if(users.count()>0):
            request.session.set_expiry(60 * 60 * 24)
            request.session["name"]         = users[0].name
            request.session["profile"]      = users[0].profile.generateMenu()  #to_json()
            request.session["profilename"]  = users[0].profile.name
            request.session["userid"]       = str(users[0].id)
            request.session["userimage"]    = users[0].getUrlImage()
            request.session["email"]        = users[0].email
            request.session["menu"]         = ""
            request.session["session_type"] = "local"
            request.session["WNotify"]      = {"message":"", "type":"", "title":""}
            return HttpResponseRedirect("/dashboard")
    return render_to_response('login/login2.html', {}, context_instance= RequestContext(request))




def validateFromGoogle(request):
    
    
    ok  = "false"
    url = "login/logout/"
    if(request.method=="POST"):
        
        users= User.objects(email=request.POST["email"])
        if(len(users)>0):
            user                            = users[0]
            user.name                       = request.POST["username"]
            user.saveImageFromUrl(request.POST["urlimage"])
            user.save()
            request.session["name"]         = user.name
            request.session["profile"]      = user.profile.generateMenu()  #to_json()
            request.session["profilename"]  = user.profile.name
            request.session["userid"]       = str(user.id)
            request.session["userimage"]    = user.getUrlImage()
            request.session["email"]        = user.email
            request.session["menu"]         = ""
            request.session["token"]        = request.POST["token"]
            request.session["session_type"] = "google"
            ok                              = "true"
            url                             = "/dashboard"
        else:
            request.session["session_type"] = "local"
    
            
    return HttpResponse(json.dumps({"ok":ok, "url": url}), content_type="application/json") 
    



def logout(request):
    del request.session["name"]
    del request.session["profile"]
    del request.session["profilename"]
    del request.session["userid"]
    del request.session["userimage"]
    del request.session["email"]
    del request.session["menu"]
    del request.session["session_type"]
    if("token" in request.session):
        del request.session["token"]
    
    return HttpResponseRedirect("/")

def userValidate(request):

    return HttpResponseRedirect("/")


def loginValidate(request):
    return HttpResponseRedirect("/")