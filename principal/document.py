from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.Auth		import googleAuth 
from apiclient.http 	import MediaFileUpload
import json




def showDocuments(request):

	token 		= googleAuth()
	newfolder 	= token.newFolder("Mi carpeta")
	token.shareDocument(newfolder['id'], "singleprojects@gmail.com", "owner")    
    #result 		= token.service.files().list().execute()
	


	return render_to_response('document/show.html', {"documents":"result"}, context_instance=RequestContext(request))