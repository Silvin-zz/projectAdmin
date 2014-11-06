from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file   import Storage
from django.conf         import settings
from principal.models    import User
from principal.models    import DayByDay
from principal.models    import DayByDayActivity

import copy
import requests
import httplib2
from datetime import datetime
import time
import oauth2client
from datetime import timedelta
from oauth2client import tools

import json


CLIENTSECRETS_LOCATION  = settings.BASE_DIR + "/auth/client_secrets.json"
REDIRECT_URI            = 'http://bravopikino.kd.io:8000/'
SCOPES                  = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/plus.login',
    'https://www.googleapis.com/auth/userinfo.email',
]


a
class calendarAPI:
    
    
    def __init__(self):
        print(SCOPES)
        self.getClientSecret()
        self.pageToken = None
        
        
    def getUrlAuthorization(self):
        
        return (self.flow.step1_get_authorize_url())
        
    
    
    def getClientSecret(self):
        with open(CLIENTSECRETS_LOCATION, 'r') as content_file:
            content = content_file.read()
        self.clientSecret       = content
        self.clientSecretArray  = json.loads(content)
        self.createFlowAuthorization()
       
        
        
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
        print(self.service)




    '''
        Listamos todos los eventos del calendario de este usuario.
    '''
        
    def listCalendarEvents(self):
        print("Iniciamos el listado :::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print  self.pageToken
        activo =True
        activities  = DayByDayActivity.objects(name="Soporte")
        activity    = activities[0]
        
            
        while True:
          #events    = self.service.events().list(calendarId='primary', pageToken=page_token, maxResults=2500, timeMax='2014-11-11T10:20:00-06:00', timeMin='2014-11-01T00:00:00-06:00').execute()
          events    = self.service.events().list(calendarId='primary', syncToken=self.pageToken, maxResults=2500).execute()
          
          
          if len(events['items']) <= 0:
              activo=False
          print("================================================================")
          for event in events['items']:
              
              print("=========================================================================")
              print(event)
              
              if "confirmed"  in event["status"]:  ############# Si es un evento confirmado
                
                localevent             = DayByDay()
                localevent.activity    = activity
                if "summary" in event:
                    localevent.title       = event["summary"].encode('utf8')
                else:
                    localevent.title       = " "
                localevent.owner       = self.user
                localevent.isCalendar  = True
                localevent.reference   = event["id"]
                
                
                if "description" in event:
                    localevent.description = event["description"].encode('utf8')
                    
                if  "dateTime" in event["start"]:                                   # tiene Hora
                    localevent.datestart   = datetime.strptime(event["start"]['dateTime'][:19]  , '%Y-%m-%dT%H:%M:%S')  
                    localevent.dateend     = datetime.strptime(event["end"]['dateTime'][:19]    , '%Y-%m-%dT%H:%M:%S')
                    localevent.calculateUsedTime()
                    localevent.save()
                    
                    
                    
                else:                                                               # no tiene hora y es todo el dia
                    
                    date_format = "%Y-%m-%d"
                    a           = datetime.strptime(event["start"]['date']  , date_format)
                    b           = datetime.strptime(event["end"]['date']    , date_format)
                    
                    delta       = b - a
                    print delta.days
                    for x in range (0,delta.days):
                        print(x)
                        newdate             = a + timedelta(days=x)
                        newevent            = copy.deepcopy(localevent)
                        newevent.datestart  = datetime.strptime(newdate.strftime("%Y-%m-%d 09:00")  , '%Y-%m-%d %H:%M')
                        newevent.dateend    = datetime.strptime(newdate.strftime("%Y-%m-%d 18:00")  , '%Y-%m-%d %H:%M')
                        newevent.calculateUsedTime()
                        newevent.save()
                        
                
               
                
                
                
               # print(localevent.dateend)
                
              
              
          page_token = events.get('nextPageToken')
          if  "nextSyncToken" in events:
              self.user.tokenSync = events["nextSyncToken"]
              self.user.save()
          print("================================================================")
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
    
    
    def getCredentialFromEmail(self,email):
        users         = User.objects(email=email)
        
        if len(users) > 0:
            self.user= users[0]
            if self.user.tokenSync == "":
                self.pageToken = None
            else:
                self.pageToken = self.user.tokenSync
                
            self.credential = oauth2client.client.Credentials.new_from_json(users[0].credential)
            if self.credential is None or self.credential.invalid == True:
                self.refreshCredential()
            self.createService()
            return True
            
        return False
            
    
    
    def refreshCredential(self):
        
        authorize_url = self.getUrlAuthorization()
        return HttpResponseRedirect(authorize_url)
    
    
    def getCredential():
        return  self.credential;
    
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
        
        
    def syncCalendar(self, email):
        
        self.getCredentialFromEmail(email)
        print("Iniciamos Sincronizacion :::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        
        body = {
          "id": uuid,
          "type": "web_hook" ,
          "token": "something_unique",
          "address": "web hook url",
          "params": {
                     "ttl" : 864000
                     }
            }
        calendar_service = get_calendar_service("silvio.bravo@enova.mx")
        resource = calendar_service.events().watch(calendarId='primary', body=body).execute()
        print(resource)
        #page_token  = None
        #events      = self.service.calendarList().watch(pageToken=page_token, maxResults=2500,body={"address":"silvio.bravo@enova.mx", "id": "primary", "type": "web_hook", "token":"za"}).execute()
        #print(events)
        
