from django.conf.urls 	import url
from django.shortcuts 	import render
from django.shortcuts 	import render_to_response
from django.template 	import RequestContext
from django.http 		import HttpResponseRedirect, HttpResponse, HttpRequest
from business.GApi	    import *
import json
import pickle




def home(request):
    gapi    = GApi()
    return HttpResponseRedirect(gapi.getURLAuthorization())
    
    
def saveCode(request):
    if("code" in request.GET):
        gapi        = GApi()
        code        = request.GET["code"]
        credential  = gapi.generateCredentialFromCode(code)
        gapi.saveTokenAndCredential(code,credential)
        print("Guardamos la credencial y el Token para este Usuario :DDDDDDD")
    return HttpResponseRedirect("/document/show")