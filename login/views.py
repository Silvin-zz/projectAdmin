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





def userList(request):

    titulo = "Hola"
    return render_to_response('userList.html',{'title' :titulo})


#Login de Usuario


def home (request):
    myuser  = User(name="Silvio")
    myuser.save()
    users   = User.objects().all()
    
    
    loginForm   = AuthenticationForm(request.POST)
#    if(request.method=="POST"):
#        loginForm   = AuthenticationForm(request.POST)
#        if( loginForm.is_valid ):
#            strUserName    = request.POST["username"]
#            strPassword    = request.POST["password"]
#            userProfile     = authenticate(username=strUserName, password=strPassword)
#            if(userProfile is not None):
#                if (userProfile.is_active):
#                    usermenu    =BMenu()
#                    login(request,userProfile)
#                    request.session["username"]     = userProfile.first_name + " " + userProfile.last_name
#                    request.session["userid"]       = userProfile.id    
#                    request.session["menu"]         = serializers.serialize("json", usermenu.getOptions(userProfile))
#                    request.session["WNotify"]      = {"message":"", "type":"", "title":""}
#                    #request.session["menu"]         = "saludos desde aqui"
#
#                    return HttpResponseRedirect("/dashboard")
#    else:
#        loginForm   = AuthenticationForm()
    return render_to_response('login/login.html', {"form" : loginForm, "users": users}, context_instance= RequestContext(request))



def userValidate(request):

    return HttpResponseRedirect("/")
