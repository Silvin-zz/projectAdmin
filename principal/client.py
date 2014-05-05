from django.conf.urls import url
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest

import json
from principal.models import Client
import time

def saveNewByAjax(request):
	client  			= Client()
	client.name 		=request.POST["name"]
	client.email 		=request.POST["email"]
	client.address		=request.POST["address"] 
	client.contactname	=request.POST["contactname"]
	client.save()
	return HttpResponse(client.to_json(), content_type="application/json")     
