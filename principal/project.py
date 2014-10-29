from django.conf.urls       import url
from django.shortcuts       import render
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
from principal.models       import Project
from principal.models       import User
from business.Auth          import googleAuth 
from django.conf            import settings
from business.GApi          import *
import time

####Projects Controllers ::::::::::::::::::::::::::::::::::::::
def projectList(request):

    bproject                    = BProject()
    return render_to_response('project/list.html', {
        "projects"      :   bproject.getAllProjects(True),
    },context_instance=RequestContext(request))



def projectAdd(request):
    request.session["WNotify"]  = {}
    userObject                  = BUser()
    projectTypeObject           = BProjectType()
    clientObject                = BClient()
    project                     = Project()
    project.datestart           = datetime.now()
    project.dateend             = datetime.now()
    project.title               = ""
    project.description         = ""
    project.code                = ""
    project.id                  = ""
    if("projectId" in request.POST):
        project         =Project.objects(pk=request.POST["projectId"]).get()
    
    

    return render_to_response('project/new.html', {

        "users"         :   userObject.getAllProjects(True),
        "projectstype"  :   projectTypeObject.getAllProjects(True),
        "clients"       :   clientObject.getAll(True),
        "project"       :   project
    },context_instance=RequestContext(request))



def projectSave(request):


    print(request.POST);
    if(request.method == "POST"):

        project                         = Project()
        if(len(request.POST["id"]) == 0):

            #gapi                        = GApi()
            totalprojects               = str(Project.objects().count())
            #projectFolder               = gapi.createFolder("PR_" + totalprojects  + "_" + request.POST["code"], "root")
            message                     = "The " + request.POST["title"] + " Project has been successfully saved"
            request.session["WNotify"]  = {"message": message, "type": "success", "title": "New Project Success"}  
            #project.folderreference     = projectFolder["id"]
            project.folderreference     = "--"

        else:

            project                     =Project.objects(pk=request.POST["id"]).get()
            message                     = "The " + request.POST["title"] + " Project has been modify"
            request.session["WNotify"]  = {"message": message, "type": "info", "title": "Update Data Project"}  


        owner                           = User.objects(pk=request.POST["owner"]).get()
        client                          = Client.objects(pk=request.POST["clientid"]).get()
        projecttype                     = Projecttype.objects(pk=request.POST['projecttypeid']).get()
        project.title                   = request.POST["title"]
        project.description             = str(request.POST["description"])
        project.client                  = client
        project.owner                   = owner
        project.typeproject             = projecttype
        project.datestart               = datetime.strptime(request.POST["datestart"],"%Y-%m-%d")
        project.dateend                 = datetime.strptime(request.POST["dateend"],"%Y-%m-%d")
        project.code                    = request.POST["code"]
        project.save()
        
    return HttpResponseRedirect("list")


    





def projectEdit(request):

    if(request.method=="POST"):
        project = Project.objects(pk=request.POST["projectId"]).get()

    return render_to_response('projects/new.html', {
                        "menuOptions"   :   json.loads(request.session["menu"]),
            })


def projectDelete(request):


    if(request.method == "POST"):

        project                    =  Project.objects(pk=request.POST["projectId"]).get()
        project.delete()
    return HttpResponse()

