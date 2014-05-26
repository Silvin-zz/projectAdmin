from django.conf 		 import settings
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from principal.models	 import driveConfiguration
import httplib2
import json
import datetime
import pickle
import time



class googleAuth():

	#global variables 

	service=""


	def __init__(self):
		self.service 	= self.requestGoogleOAuthToken()
		self.trynumber	=0


	# def saveServiceObject(self, driveObject, serviceObject):
	# 	driveObject.active		=True
	# 	driveObject.datestart	=datetime.datetime.now()
	# 	driveObject.save()
	# 	with open(settings.BASE_DIR + "/auth/credential", 'wb') as input:
	# 		tmpservice= pickle.dump(serviceObject,input, -1)
	# 	return serviceObject


	# def getToken(self):

	# 	driveconf 	= driveConfiguration.objects()		
	# 	if (len(driveconf) == 0):

	# 		driveObject				= driveConfiguration()
	# 		driveObject.active 		= False;
	# 		driveObject.datestart	= datetime.datetime.now().time()
	# 		return  self.saveServiceObject(driveObject,self.requestGoogleOAuthToken())  
	# 	elif (driveconf[0].active ==True):
	# 		differencetime	=  datetime.datetime.now() - driveconf[0].datestart
	# 		if( float(differencetime.seconds/3600) > 1):
				
	# 			driveconf[0].active		=False
	# 			driveconf[0].save()
	# 			return self.saveServiceObject(driveconf[0], self.requestGoogleOAuthToken)
	# 		else:

	# 			with open(settings.BASE_DIR + "/auth/credential", 'rb') as input:
	# 				tmpservice= pickle.load(input)
	# 			return tmpservice
	# 	else:
	# 		time.sleep(5)
	# 		self.getToken()



	def requestGoogleOAuthToken(self):
		
		sourceKey	= settings.BASE_DIR + "/auth/b054caf6c564d84ff0396f4b42b7d928551adfeb-privatekey.p12"
		f 			= file(sourceKey, 'rb')
		key 		= f.read()

		f.close()
		print(datetime.datetime.now().time())										
		credentials = SignedJwtAssertionCredentials('952570055288-qfd3i1aqe3fa2ffa7bujl1oagla52ceg@developer.gserviceaccount.com',
	                                                key,
	                                                scope='https://www.googleapis.com/auth/drive.file')
		http 	= httplib2.Http()
		http 	= credentials.authorize(http)
		service = build('drive', 'v2', http=http)
		return service


	def newFolder(self, title, parentId=""):
		resorce 	={}
		if ("" in parentId):
			resource = { 'title': title, "mimeType": "application/vnd.google-apps.folder" }
		else:
			resource = { 'title': title, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id":parentId}] }

		newdoc 			= self.service.files().insert( body=resource).execute()
		return newdoc


	def shareDocument(self, documentId, userEmail,role):
		new_permission  = { 'value': userEmail, 'type': "user", 'role': role }
		result 			= self.service.permissions().insert( fileId= documentId, body=new_permission).execute()
		print(datetime.datetime.now().time())




	#get a list form query 

	def getList(self, query):
		return self.service.files().list(q=query).execute()

