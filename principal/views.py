from django.conf.urls import url
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response     # Para poder tener acceso al request dentro de la vista por ejemplo
                                                    # Tener acceso a las variables de session :D
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

import json



def index(request):
    return render_to_response('dashboard/index.html', {"dato":request.session["name"]}, context_instance=RequestContext(request))


####Task Controllers ::::::::::::::::::::::::::::::::::::::



def tasksAdmin(request):
    return render_to_response('tasks/admin.html', {"menuOptions" :  json.loads(request.session["menu"]), "saludo":json.loads(request.session["menu"])})


####Team  Controllers ::::::::::::::::::::::::::::::::::::::


def teamList(request):
    return render_to_response('teams/list.html', {"menuOptions" :  json.loads(request.session["menu"]), "saludo":json.loads(request.session["menu"])})



####Documents Controllers ::::::::::::::::::::::::::::::::::::::

def documentList(request):
    return render_to_response('documents/list.html', {"menuOptions" :  json.loads(request.session["menu"]), "saludo":json.loads(request.session["menu"])})


####DashBoard Controllers ::::::::::::::::::::::::::::::::::::::

def dashboardList(request):
    return render_to_response('dashboard/index.html', {"menuOptions" :  json.loads(request.session["menu"]), "saludo":json.loads(request.session["menu"])})