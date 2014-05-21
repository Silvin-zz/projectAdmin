from django.conf 		 import settings
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import httplib2


class googleAuth():

	def getToken(self):
		sourceKey	= settings.BASE_DIR + "/auth/b054caf6c564d84ff0396f4b42b7d928551adfeb-privatekey.p12"
		f 			= file(sourceKey, 'rb')
		key 		= f.read()

		f.close()
												
		credentials = SignedJwtAssertionCredentials('952570055288-qfd3i1aqe3fa2ffa7bujl1oagla52ceg@developer.gserviceaccount.com',
	                                                key,
	                                                scope='https://www.googleapis.com/auth/drive.file')
		http = httplib2.Http()
		http = credentials.authorize(http)
		return build('drive', 'v2', http=http)
