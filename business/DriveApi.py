from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from django.conf 		 import settings
import base64
import httplib2

import json


# from google API console - convert private key to base64 or load from file





class DriveApi:

	def __init__(self):
		self.service	=""
		self.trynumber	=0



	def InitialLogin(self):
		sourceKey	= settings.BASE_DIR + "/auth/b054caf6c564d84ff0396f4b42b7d928551adfeb-privatekey.p12"
		id 			= "952570055288-qfd3i1aqe3fa2ffa7bujl1oagla52ceg@developer.gserviceaccount.com"
		f 			= file(sourceKey, 'rb')
		key 		= f.read()
		http 		= httplib2.Http()
		credentials = SignedJwtAssertionCredentials(id, key, scope='https://www.googleapis.com/auth/drive')
		credentials.authorize(http)

		gauth 				= GoogleAuth()
		gauth.credentials 	= credentials
		drive 				= GoogleDrive(gauth)
		self.service		=drive



	def Login(self, code):
		gauth = GoogleAuth()
		gauth.Auth(code)
		self.service = GoogleDrive(gauth)
		print(self.service)



# Create authentication url user needs to visit

	def getURL(self):
		gauth = GoogleAuth()
		auth_url = gauth.GetAuthUrl() 
		return auth_url





	def newFolder(self,  title, parentId):

		resorce 	={}
		if ("" in parentId):
			resource = { 'title': title, "mimeType": "application/vnd.google-apps.folder" }
		else:
			resource = { 'title': title, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id":parentId}] }
		folder = (self.service.CreateFile(resource))
		folder.Upload()
		return (folder)


	def getList(self, query):
		return self.service.ListFile({'q': query}).GetList()



	def shareDocument(self, documentId, userEmail,role):
		print(documentId)
		shareFile=self.service.CreateFile({'id': documentId})
		newOwner={
				'value': "singleprojects@gmail.com",
      			'type': "user",
      			'role': "owner"
			}
		print(newOwner)
		shareFile["permissions"].append(newOwner)
		print("INICIAMOS::::::::::::::::::::::")
		try:
			shareFile.Upload()
		except Exception, e:
			print("No Pudimos")
			print "Couldn't do it: %s" % e
		print(shareFile)

		# new_permission  = { 'value': userEmail, 'type': "user", 'role': role }
		# result 			= self.service.permissions().insert( fileId= documentId, body=new_permission).execute()
		# print(datetime.datetime.now().time())