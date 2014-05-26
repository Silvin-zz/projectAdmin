from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.Auth		import googleAuth 
from apiclient.http 	import MediaFileUpload
import json




def showDocuments(request):

	return render_to_response('document/show.html', {}, context_instance=RequestContext(request))


def getList(request):
	# folder 			= request.POST["folderId"]
	folder 				="0B5Z_u9bE4oZlOVNrd0ppZEpRM2c"
	query 			= ""

	token 			= googleAuth()
	response_data 	= token.getList(query)
	print(json.dumps(response_data))
	return render_to_response('document/list.html', {"list": response_data}, context_instance=RequestContext(request))
	# print(json.dumps(response_data))
	# return HttpResponse(json.dumps(response_data), content_type="application/json")
	
def newFolder(request):
	token 			= googleAuth()
	newFolder		= token.newFolder(request.POST["title"], request.POST["folderIdParent"]);
	token.shareDocument(newFolder["id"], "singleprojects@gmail.com","owners")
	return render_to_response('document/folder.html', {"document": newFolder}, context_instance=RequestContext(request))