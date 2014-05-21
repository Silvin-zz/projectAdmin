from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.Auth		import googleAuth 
from apiclient.http 	import MediaFileUpload
import json




def showDocuments(request):
	# client = gdata.docs.service.DocsService()
	# client.ClientLogin('singleprojects@gmail.com', 's1ngl3pr0j3ct')
	# documents_feed 	= client.GetDocumentListFeed()
	token 		= googleAuth()
	service 	=token.getToken()
	resource = { 'title': 'Datos Ventas', "mimeType": "application/vnd.google-apps.folder" }
	
    resource = {
        'title': "Datos Ventas",
        "mimeType": "application/vnd.google-apps.folder",
  	}
  	
  	
  	newdoc = service.files().insert(
        body=resource,
    ).execute()
    
    new_permission = {
  	    'value': "singleprojects@gmail.com",
  	    'type': "user",
  	    'role': "owner",
    }
    
	
	result = service.permissions().insert(
        fileId= newdoc['id'], body=new_permission).execute()
        
        
    result = service.files().list().execute()
	
  	
    
  	
  	
  	#result = service.files().insert(
    #    body=resource,
    #).execute()
    # Respond with the new file id as JSON.
    # self.RespondJSON(resource['id'])
	

	#client.CreateFolder("Example",)
	# print(client.CreateFolder("UNO"))
	#client.CreateFolder("DOS", "Example",)


	return render_to_response('document/show.html', {"documents":result}, context_instance=RequestContext(request))