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






def userList(request):

    titulo = ""
    return render_to_response('userList.html',{'title' :titulo})


#Login de Usuario


def home (request):
    
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
    
    
    
    
    
    if(request.method=="POST"):
        
        
        print(Menu.objects)
        
        users   =   User.objects(username=request.POST["username"], password=request.POST["password"])
        if(users.count()>0):
            request.session.set_expiry(60 * 60 * 24)
            request.session["name"]         = users[0].name
            request.session["profile"]      = users[0].profile
            request.session["userid"]       = str(users[0].id)
            request.session["userimage"]    = users[0].getUrlImage()
            request.session["email"]        = users[0].email
            request.session["menu"]         = ""
            request.session["WNotify"]      = {"message":"", "type":"", "title":""}
            return HttpResponseRedirect("/dashboard")
    return render_to_response('login/login.html', {}, context_instance= RequestContext(request))



def userValidate(request):

    return HttpResponseRedirect("/")
