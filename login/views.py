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





def userList(request):

    titulo = "Hola"
    return render_to_response('userList.html',{'title' :titulo})


#Login de Usuario


def home (request):

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
            request.session["menu"]         = ""
            request.session["WNotify"]      = {"message":"", "type":"", "title":""}
            return HttpResponseRedirect("/dashboard")
    return render_to_response('login/login.html', {}, context_instance= RequestContext(request))



def userValidate(request):

    return HttpResponseRedirect("/")
