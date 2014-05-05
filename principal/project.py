from django.conf.urls       import url
from django.shortcuts       import render

# Create your views here.
from django.shortcuts       import render_to_response
from django.template        import RequestContext
from django.http            import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime               import datetime

import json

from business.project       import BProject
from business.user          import BUser
from business.projecttype   import BProjectType
from business.client        import BClient
from principal.models       import Project
from principal.models       import Client
from principal.models       import Projecttype
from principal.models       import User

import time

####Projects Controllers ::::::::::::::::::::::::::::::::::::::
def projectList(request):

    bproject                    = BProject()
    wNotify                     = request.session["WNotify"]
    request.session["WNotify"]  = {"message":"", "type":"", "title":""}


    return render_to_response('projects/list.html', {
        "projects"      :   bproject.getAllProjects(True),
        "WNotify"       :   wNotify
    },context_instance=RequestContext(request))



def projectAdd(request):

    userObject          = BUser()
    projectTypeObject   = BProjectType()
    clientObject        = BClient()

    return render_to_response('projects/new.html', {

        "users"         :   userObject.getAllProjects(True),
        "projectstype"  :   projectTypeObject.getAllProjects(True),
        "clients"       :   clientObject.getAll(True),
        "datestart"     :   time.strftime("%Y-%m-%d"),
        "dateend"       :   time.strftime("%Y-%m-%d"),
        "id"            :   "",
    },context_instance=RequestContext(request))



def projectSave(request):




    if(request.method == "POST"):
         
        owner       = User.objects(pk=request.POST["owner"]).get()
        client      = Client.objects(pk=request.POST["clientid"]).get()
        projecttype = Projecttype.objects(pk=request.POST['projecttypeid']).get()
        
        project                 = Project()
        project.title           = request.POST["title"]
        project.description     = str(request.POST["description"])
        project.client          = client
        project.owner           = owner
        project.projecttypeid   = projecttype
        project.datestart       = datetime.strptime(request.POST["datestart"],"%Y-%m-%d")
        project.dateend         = datetime.strptime(request.POST["dateend"],"%Y-%m-%d")
        project.save()
        message                     = "The " + request.POST["title"] + " Project project successfully saved"
        request.session["WNotify"]  = {"message": message, "type": "success", "title": "New Project Success"}

        


    return HttpResponseRedirect("list")




def projectEdit(request):

    return render_to_response('projects/new.html', {
                        "menuOptions"   :   json.loads(request.session["menu"]),
            })


def projectDelete(request):

    return render_to_response('projects/new.html', {
                        "menuOptions"   :   json.loads(request.session["menu"]),
            })