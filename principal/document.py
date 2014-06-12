from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.DriveApi	import DriveApi 
from business.Auth      import googleAuth
from business.OAuth2	import *
from business.GApi	    import *
from principal.models   import driveConfiguration
from apiclient.discovery import build
import json
import pickle





def showDocuments(request):
	
	return render_to_response('document/show.html', {}, context_instance=RequestContext(request))
	



def getList(request):

	query 			= "'" + request.POST["folderId"] + "' in parents"
	gapi            = GApi()
	response_data	= gapi.find(query)
	print(response_data)
	return render_to_response('document/list.html', {"list": response_data}, context_instance=RequestContext(request))
	
	
def newFolder(request):
    gapi            = GApi()
    newFolder       = gapi.createFolder(request.POST["title"], request.POST["folderIdParent"])
    gapi.shareItem(newFolder["id"],request.session["email"], "writer")
    return render_to_response('document/folder.html', {"document": newFolder}, context_instance=RequestContext(request))
	


def getProjectAccountToken(request):
    print("Llegamos::::")
    credential=getAPICredential()
    return HttpResponse(credential.to_json(), content_type="application/json") 


def upload(request):
	return render_to_response('document/upload.html', {}, context_instance=RequestContext(request))
	


def shareItem(request):
    gapi    = GApi()
    gapi.generateService()
    email   = request.session["email"]
    if("email" in request.POST and "" not in request.POST["email"]):
        email=request.POST["email"]
    result  =gapi.shareItem(request.POST["itemId"], email, request.POST["role"])
    return HttpResponse(result, content_type="application/json")
    