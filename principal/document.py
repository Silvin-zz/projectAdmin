from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
import json

import gdata.docs.service


def showDocuments(request):
	client = gdata.docs.service.DocsService()
	client.ClientLogin('singleprojects@gmail.com', 's1ngl3pr0j3ct')
	documents_feed 	= client.GetDocumentListFeed()
	#client.CreateFolder("Example",)
	print(client.CreateFolder("UNO"))
	#client.CreateFolder("DOS", "Example",)


	return render_to_response('document/show.html', {"documents":documents_feed.entry}, context_instance=RequestContext(request))