from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.DriveApi	import DriveApi 
from business.Auth      import googleAuth
from business.OAuth2	import *
from principal.models   import driveConfiguration
from apiclient.discovery import build
import json
import pickle





def showDocuments(request):
	code= ""
	# print("Ingresa a tu cuenta de google scon singleprojects@gmail.com, Copia esta url en tu navegador y Guarda este token dentro de la base de datos :)")
	# print(get_authorization_url("singleprojects@gmail.com",2))
	query 			= "'root' in parents"
	print("Nos Logeamos para solicitar el servicio :))))")
	service			=getAPIService()
	print("Obtenemos el servicio")
	print(service)
	response_data	= service.files().list(q=query).execute()
	print(response_data)
	return render_to_response('document/show.html', {}, context_instance=RequestContext(request))
	



def getList(request):

	query 			= "'" + request.POST["folderId"] + "' in parents"
	print("Nos Logeamos para solicitar el servicio :))))")
	service			=getAPIService()
	print("Obtenemos el servicio")
	print(service)
	response_data	= service.files().list(q=query).execute()
	print(response_data)
	# DApi=googleAuth()
	# DApi 			= DriveApi()
	# DApi.InitialLogin()
	# response_data 	= DApi.getList(query)
	# print(response_data)
	return render_to_response('document/list.html', {"list": response_data}, context_instance=RequestContext(request))
	
	
def newFolder(request):
	service			=getAPIService()

	resource 		= { 'title': request.POST["title"], "mimeType": "application/vnd.google-apps.folder", "parents": [{"id":request.POST["folderIdParent"]}] }
	print("Creamos un FOLDER")
	print(resource)
	newFolder 			= service.files().insert( body=resource).execute()
	print("Terminamos de crear el FOLDER")
	return render_to_response('document/folder.html', {"document": newFolder}, context_instance=RequestContext(request))
	


def getProjectAccountToken(request):
    print("Llegamos::::")
    credential=getAPICredential()
    return HttpResponse(credential.to_json(), content_type="application/json") 


def upload(request):
	return render_to_response('document/upload.html', {}, context_instance=RequestContext(request))
    