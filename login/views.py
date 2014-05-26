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






def userList(request):

    titulo = ""
    return render_to_response('userList.html',{'title' :titulo})


#Login de Usuario


def home (request):


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
