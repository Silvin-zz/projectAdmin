from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file   import Storage
from django.conf         import settings
from principal.models    import User
import requests
import httplib2
from datetime import datetime
import time


import json


CLIENTSECRETS_LOCATION  = settings.BASE_DIR + "/auth/client_secrets.json"
REDIRECT_URI            = 'http://bravopikino.kd.io:8000/'
SCOPES                  = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.email',
]



class calendarAPI:
    
    
    def __init__(self):
        print(SCOPES)
        self.getClientSecret()
        
        
    
    
    def getClientSecret(self):
        with open(CLIENTSECRETS_LOCATION, 'r') as content_file:
            content = content_file.read()
        self.clientSecret       = content
        self.clientSecretArray  = json.loads(content)
        print("--------------------------------------------------")
        self.createFlowAuthorization()
        print(self.flow.step1_get_authorize_url())
        
        
    def createFlowAuthorization(self):
        self.flow = OAuth2WebServerFlow(
             self.clientSecretArray["web"]["client_id"],
             self.clientSecretArray["web"]["client_secret"],
             ' '.join(SCOPES),
             redirect_uri=self.clientSecretArray["web"]["redirect_uris"][0]
        )
        
    def createCredential(self, code):
        self.credential = self.flow.step2_exchange(code)
        self.createService()
        return self.credential
        
        
    def createService(self):
        http         = httplib2.Http()
        http         = self.credential.authorize(http)
        self.service = build('calendar', 'v3', http=http)
        self.listCalendar()
        
    def listCalendar(self):
        page_token = None
        while True:
          events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
          for event in events['items']:
              time_tuple = time.strptime(event.end.dateTime, "%Y-%m-%d %H:%M:%S")
              print repr(time_tuple)
          page_token = events.get('nextPageToken')
          if not page_token:
            break
        
        
    def getUserInfo(self):
        r = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token=" + self.credential.access_token)
        #this gets the google profile!!
        return r.content
    '''
        hasta aqui es puro logeo , es decir se pueden ocupar estas mismos metodos para logearse ara cualquier
        api de google hasta aqui es solo oauth2
        
        
        
    '''
    
    
    
    def validateCredential(self):
        
        if self.credential is None or self.credential.invalid == True:
            self.credential = run(FLOW, self.credential)
    
    def generareService(self):
        self.http = httplib2.Http()
        self.http = self.credential.authorize(self.http)
        
        
    def  getCalendarEvents(self):
        print("saludos")
        
        

        #service = build(serviceName='calendar', version='v3', http=http,developerKey='YOUR_DEVELOPER_KEY')
        
    def getCalendars(self):
        print("Buscando los calendarios :D")
        
        
        
    

        
