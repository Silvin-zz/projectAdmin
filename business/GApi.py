

import logging
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from django.conf         import settings
from principal.models    import driveConfiguration
import json
import httplib2
import oauth2client






class GApi():
    
    """
        Variables publicas de la clase
    """
    
    service     =""
    tokenObject =""
    credential  =""
    
    
    
    """
        Constructor de la clase
    """
    
    def __init__(self):
        if(self.tokenExist()==True):
            self.getCredencial()
        
    
    
    
    
    """
        Guardamos el token en la base de datos
    """
    def saveToken(self):
        a=""
    
    
    
    
    
    """
        Obtenemos el token  guardado en la base de datos
    """
    
    def getToken(self):
        a=""
    
   
   
   
    
    
    """
        Generamos una credencial para poder solicitar un servicio 
        
    """
    
    def getCredencial(self):
        
        self.credential = oauth2client.client.Credentials.new_from_json(self.tokenObject.credential)
    
    
    
    
    
        
    """
        Generamos un servicio para poder utilizarlo al momento de hacer operaciones
        sobre los items 
    """
    
    
    def generateService(self):
        
        if("" in self.service):
            http            = httplib2.Http()
            http            = self.credential.authorize(http)
            self.service    = build('drive', 'v2', http=http)
    
    
    
    """
        Validamos si un token existe
    """
        
        
    def tokenExist(self):
        
        objs                = driveConfiguration.objects()
        self.tokenObject    = objs[0]
        
        if(self.tokenObject.active==True):
            return True
        else:
            return False
    
    
    
    

    """
        Refrescamos el token de acceso para el caso de uso del token a traves de javascript
    """
    
    def refreshToken(self):
        
        http = httplib2.Http()
        try:
            cred2=self.credential.refresh(http)
        except errors.HttpError, e:
            print('An error occurred: %s', e)
            
        self.tokenObject.credential=self.credential.to_json()
        self.tokenObject.save()
    
    
    """
        Realizamos una consulta al api de google drive :)
        
    """
    
    
    def find(self, query):
        self.generateService()
        return(self.service.files().list(q=query).execute())
    
    
    
    """
        Compartimos un item (Folder o Carpeta) con id de usuario disponible :D
    """
    
    def shareItem(self):
        self.generateService()
    
    
    
    """
        Creamos un folder 
    """
        
    def createFolder(self, title, parentId):
        self.generateService()
        resource 		= { 'title': title, "mimeType": "application/vnd.google-apps.folder", "parents": [{"id": parentId }] }
        newFolder 		= self.service.files().insert( body=resource).execute()
        return (newFolder)  