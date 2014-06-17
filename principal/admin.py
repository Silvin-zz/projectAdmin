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
from business.Mail    import Mail
import random
from bson import json_util

## models necesaryes from work with a TASK, sorry for my bad english :(



from principal.models import Task

############### USER #######


def userList(request):
    users= User.objects()
    profiles= Profile.objects()
    return render_to_response('user/list.html', {"users":users, "profiles":profiles}, context_instance=RequestContext(request))

def userNew(request):
    result={"success":"false", "message":"", "data":""}
    print("Iniciamos::::::::::::::::::::")
    
    if( "new" in request.POST["userAction"]):
        users           = User.objects(email=request.POST["userEmail"])
        if(len(users)>0):
            result["message"]="Ya existe un usuario con el correo electronico: " + str(request.POST["userEmail"])
        else:
            user            = User()
            profile         = Profile.objects(pk=request.POST["userProfile"]).get()
            user.name       = request.POST["userName"]
            user.email      = request.POST["userEmail"]
            user.username   = request.POST["userEmail"]
            user.password   = str(random.randrange(10000,99999)) + "SP" + str(random.randrange(10000,99999))
            user.profile    = profile
            user.save()
            mail            = Mail()
            #mail.newUser(user)
            result["message"]  = "El usuario se ha registrado correctamente"
            result["success"]  = "true"
            result["data"]     = {"id":str(user.id), "name":user.name, "profile": user.profile.name,  "username": user.username, "email":user.email, "image": user.getUrlImage()}
        
        return HttpResponse(json.dumps(result), content_type="application/json") 


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





