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
    
    
    #menu= Menu()
    #menu.name            = "Targets"
    #menu.url             = "/target/list/"
    #menu.iconclass       = "glyphicon glyphicon-screenshot"
    #menu.save()
    
    #profile             =Profile()
    #profile.name        ="Administrator"
    #profile.options     =[menu]
    #profile.save()
    
    # drive  = driveConfiguration()
    # drive.credential="{\"_module\": \"oauth2client.client\", \"token_expiry\": \"2014-05-26T05:49:39Z\", \"access_token\": \"ya29.IgCImXaOM88F9xoAAAAqWEzWg5pqF_7JONWBJtBCOoSnNoa4oUmN2Nzla7klSA\", \"token_uri\": \"https://accounts.google.com/o/oauth2/token\", \"invalid\": false, \"token_response\": {\"access_token\": \"ya29.IgCImXaOM88F9xoAAAAqWEzWg5pqF_7JONWBJtBCOoSnNoa4oUmN2Nzla7klSA\", \"token_type\": \"Bearer\", \"expires_in\": 3600, \"refresh_token\": \"1/_tkmi9tXUaY6OmEUjzG53-LcVBOe3-UHRA3cSeau-DE\", \"id_token\": {\"sub\": \"118382467861745398798\", \"cid\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\", \"iss\": \"accounts.google.com\", \"email_verified\": true, \"id\": \"118382467861745398798\", \"at_hash\": \"_kg1-ot_hyrksYgny-m7JA\", \"exp\": 1401083381, \"azp\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\", \"iat\": 1401079481, \"verified_email\": true, \"token_hash\": \"_kg1-ot_hyrksYgny-m7JA\", \"email\": \"singleprojects@gmail.com\", \"aud\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\"}}, \"client_id\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\", \"id_token\": {\"sub\": \"118382467861745398798\", \"cid\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\", \"iss\": \"accounts.google.com\", \"email_verified\": true, \"id\": \"118382467861745398798\", \"at_hash\": \"_kg1-ot_hyrksYgny-m7JA\", \"exp\": 1401083381, \"azp\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\", \"iat\": 1401079481, \"verified_email\": true, \"token_hash\": \"_kg1-ot_hyrksYgny-m7JA\", \"email\": \"singleprojects@gmail.com\", \"aud\": \"952570055288-14thfi8q8jbanlaq1kfvekl9nsk5cucq.apps.googleusercontent.com\"}, \"client_secret\": \"06ILhZBgt7-RAJfnu0FCx7zD\", \"revoke_uri\": \"https://accounts.google.com/o/oauth2/revoke\", \"_class\": \"OAuth2Credentials\", \"refresh_token\": \"1/_tkmi9tXUaY6OmEUjzG53-LcVBOe3-UHRA3cSeau-DE\", \"user_agent\": null}"
    # drive.token= "4/qRwMw8KAfHr3QTRRlS2892e0Hunu.0pK8PQimUIcXEnp6UAPFm0FglrxtjAI"
    # drive.active=True;
    # drive.save()


    # pr = PriorityTask()
    # pr.name= "Fire"
    # pr.number=1
    # pr.classname="danger"
    # pr.save()


    # pr = PriorityTask()
    # pr.name= "High"
    # pr.number=2
    # pr.classname="warning"
    # pr.save()

    # pr = PriorityTask()
    # pr.name= "Medium"
    # pr.number=3
    # pr.classname="info"
    # pr.save()

    # pr = PriorityTask()
    # pr.name= "Low"
    # pr.number=4
    # pr.classname="success"
    # pr.save()

    #tg = TargetType()
    #tg.name="Entrega"
    #tg.save()

    #tg = TargetType()
    #tg.name="Analisis de Software"
    #tg.save()


    #tg = TargetType()
    #tg.name="Diseno de Software"
    #tg.save()

    #tg = TargetType()
    #tg.name="Testing de Software"
    #tg.save()


    #user    = User()
    #user.name="Silvio Bravo Cado"
    #user.username="admin"
    #user.password="pass"
    #user.save()
    
    
    #projecttype= Projecttype()
    #projecttype.name="Desarrollo de Software"
    #projecttype.active=True
    #projecttype.save()
    
    
    
    
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
            request.session["profile"]      = users[0].profile.generateMenu()  #to_json()
            request.session["profilename"]  = users[0].profile.name()
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
    if  "google" in request.session["session_type"]:
        access_token    = request.session["token"]
        url             = 'https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout'
        h               = httplib2.Http()
        result          = h.request(url, 'GET')[0]
    return HttpResponseRedirect("https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://bravopikino.kd.io:8000/")

def userValidate(request):

    return HttpResponseRedirect("/")


def loginValidate(request):
    return HttpResponseRedirect("/")