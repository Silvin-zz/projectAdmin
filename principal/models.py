# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from datetime import datetime
from mongoengine import *
from mongoengine.django.auth import User
from django.core.urlresolvers import reverse
from datetime import datetime
from decimal import *

from django.conf import settings
import os
import bson
import datetime
import urllib




class Company(Document):
    name            = StringField(max_length=500, required=True)
    description     = StringField(max_length=2000)


class Taskcomment(Document):
    comment         = StringField(max_length=2000)
    meta            = {'allow_inheritance': True}
    
    
class AuthUser(Document):
    first_name      = StringField(max_length=2000)
    meta            = {'allow_inheritance': True}

#Manejo de Menus


class Client(Document):
    name            = StringField()
    address         = StringField()
    contactname     = StringField()
    email           = EmailField()

    meta = {'allow_inheritance': True}

class Menu(Document):
    name            = StringField()
    url             = StringField()
    iconclass       = StringField()
    isFather        = BooleanField()
    subItem         = StringField() 
    meta            = {'allow_inheritance': True}
    
    
    def getMyFather(self):
        
        if("" in str(self.subItem)):
            
            return "None"
            
        else:
            
            father= Menu.objects(pk=self.subItem).get()
            return father.name
        

class Profile(Document):
    name           = StringField()
    options        = ListField(ReferenceField(Menu))
    meta           = {'allow_inheritance': True}
    def totalOptions(self):
        return(len(self.options))
        
    def generateMenu(self):
        vtmenu              ={}
        vtmenu["options"]   =[]
        vtoptions           =[]
        
        for myoption in self.options:
            vtoptions.append(myoption.id)
        
        
        
        for option in Menu.objects(pk__in=vtoptions).order_by("_id") :
            
            if(len(option.subItem.strip()) <= 0 ):
                    
                vtmenu["options"].append({"name":option.name,  "icon": option.iconclass, "url": option.url, "father":False})
            else:
                father=Menu.objects(pk=option.subItem).get()
                if(father.name not in vtmenu):
                    vtmenu[father.name]             ={}
                    vtmenu[father.name]["name"]     =father.name
                    vtmenu[father.name]["icon"]     =father.iconclass
                    vtmenu[father.name]["url"]      ="#"
                    vtmenu[father.name]["father"]   =True
                    vtmenu[father.name]["options"]  =[]
                    
                vtmenu[father.name]["options"].append({"name":option.name,  "icon": option.iconclass, "url": option.url, "father":False})
                
        return vtmenu
                
            
        
        
        


class User(Document):

    name            = StringField(max_length=2000)
    username        = StringField(max_length=2000)
    password        = StringField()
    profile         = ReferenceField(Profile)
    active          = BooleanField()
    email           = EmailField()
    urlimage        = StringField(default="")
    token           = StringField(default="")
    imageextension  = StringField(default="png")
    meta            = {'allow_inheritance': True}
    
    def getUrlImage(self):
        
        if(os.path.isfile(settings.STATICFILES_USER_IMAGES_DIRS[0] + "/" + str(self.id) + "." + str(self.imageextension))):
            return (str(self.id) + "." + str(self.imageextension))
        return ("1.png")
        
        
        
    def saveImageFromUrl(self, url):
       
        extension           = url.split(".")[-1]
        self.imageextension = extension
        resource            = urllib.urlopen(url)
        filename            = os.path.join(settings.STATICFILES_USER_IMAGES_DIRS[0] + "/" + str(self.id) + "." + str(extension))
        output              = open(filename,"ab")
        output.write(resource.read())
        os.chmod(filename, 0777)
        print("Guardamos.")
        output.close()
        
        


#Terminamos el manejo de usuarios.




    
class Projecttype(Document):
    name            = StringField(max_length=2000)
    active          = BooleanField()
    meta            = {'allow_inheritance': True}





class Project(Document):

    title           = StringField(max_length=2000)
    description     = StringField()
    code            = StringField()
    active          = BooleanField(default= True)
    client          = ReferenceField(Client)
    typeproject     = ReferenceField(Projecttype)
    datestart       = DateTimeField()
    dateend         = DateTimeField()
    realdatestart   = DateTimeField()
    realdateend     = DateTimeField()
    owner           = ReferenceField(User)
    inuse           = BooleanField(default=True)
    active          = BooleanField(default=True)
    totaltargets    = IntField(default=0)
    totalendtargets = IntField(default=0)
    advancepercent  = DecimalField(default=0)
    priority        = IntField(default=1)
    meta            = {'allow_inheritance': True}
    key             = StringField(default="")
    folderreference = StringField(default="")

    def getShortDescription(self):
        return (self.description[:130] + " ...") if(len(self.description)>130) else self.description
        
    def dateDiff(self):
        difference = self.dateend - self.datestart
        return difference.days

    def timePercent(self):
        difference      = self.dateend - self.datestart
        realdifference  = datetime.datetime.now() - self.datestart
        if(self.datestart.date() > datetime.datetime.now().date() ):
            return 0
        if(datetime.datetime.now().date() >= self.dateend.date()):
            return 100
        return round(float(float(100) / float(difference.days)) * float(realdifference.days))

    def getTotalEndTargets(self):
        targets             = Target.objects(project=self, finished= True)
        self.totalendtargets= len(targets)
        return self.totalendtargets

    def getTotalTargets(self):
        targets             = Target.objects(project=self)
        self.totaltargets   = len(targets)
        return self.totaltargets




    def endPercent(self):
        if(self.totaltargets >0):
            return  round((Decimal(100) / Decimal(self.totaltargets)) * self.totalendtargets,2)
        return 0



    meta = {'allow_inheritance': True}    
    






class Stage(Document):
    name            = StringField()


class TaskType(Document):
    name            = StringField()



class PriorityTask(Document):
    name            = StringField()
    number          = IntField()
    classname       = StringField()



############## ATTR FROM TASK


class Comment(EmbeddedDocument):
    description     = StringField()
    date            = DateTimeField(default=datetime.datetime.now)
    owner           = ReferenceField(User)





class TimeLine(EmbeddedDocument):
    hoursspend      = FloatField()
    activity        = StringField()
    endpercent      = IntField()
    urlreference1   = StringField()
    urlreference2   = StringField()
    dateadd         = DateTimeField(default=datetime.datetime.now)
    date            = DateTimeField(default=datetime.datetime.now)
    owner           = ReferenceField(User)





class Task (Document):
    title           = StringField(max_length=2000)
    description     = StringField()
    code            = StringField(default= "")
    active          = BooleanField(default=True)
    owner           = ReferenceField(User)
    comments        = SortedListField(EmbeddedDocumentField(Comment), ordering="date")
    datestart       = DateTimeField()
    dateend         = DateTimeField()
    realdatestart   = DateTimeField()
    realdateend     = DateTimeField()
    dateadd         = DateTimeField()
    tasktype        = ReferenceField(TaskType)
    endpercent      = IntField(default=0)
    estimatedhours  = FloatField(default=0)
    hoursspend      = FloatField(default=0)
    usedhours       = FloatField(default=0)
    iscritical      = BooleanField(default= False)
    finished        = BooleanField(default= False)
    priority        = ReferenceField(PriorityTask)
    timeline        = SortedListField(EmbeddedDocumentField(TimeLine), ordering="dateadd")
    folderreference = StringField(default="")
    meta            = {'allow_inheritance': True}

    def getShortDescription(self):
        return (self.description[:130] + " ...") if(len(self.description)>130) else self.description


    def updateHoursSpend(self, newhours):
        print("Iniciamos::::::::::::::")
        print(newhours)
        print(self.usedhours)
        self.usedhours  =float(self.usedhours) + float(newhours)
        self.save()
        print("terminamos:S:S:S:S:S:S:S:S:S:S:")

    def updateEndPercent(self, endpercent):
        
        self.endpercent=int(endpercent)
        if(self.endpercent == 100):
            self.finished       = True
            self.realdateend    = datetime.datetime.now().date()
        self.save()

    def getTaskLive(self):
        difference      = self.dateend - self.datestart
        realdifference  = datetime.datetime.now() - self.datestart
        if(self.datestart.date() > datetime.datetime.now().date() ):
            print("Entramos 1")
            return 0
        if(datetime.datetime.now().date() >= self.dateend.date()):
            print("Entramos 2")
            return 100
        print("Entramos 3")
        return round(float(float(100) / float(difference.days)) * float(realdifference.days))
    
    
    def daysLeft(self):
        if(self.finished == False):
            realdifference  = self.dateend.date() -datetime.datetime.now().date()
            return realdifference.days
        else:
            realdifference  = self.dateend -datetime.datetime.now()
            return  0
        




class TargetType(Document):
    name            = StringField()




class Target(Document):
    title           = StringField(max_length=2000)
    description     = StringField()
    code             = StringField(default="")
    targettype      = ReferenceField(TargetType)
    owner           = ReferenceField(User)
    project         = ReferenceField(Project)
    datestart       = DateTimeField()
    dateend         = DateTimeField()
    realdatestart   = DateTimeField(required=False)
    realdateend     = DateTimeField(required=False)
    endpercent      = IntField(default=0)
    comments        = ListField(EmbeddedDocumentField(Comment), required=False)
    finished        = BooleanField(default = False)
    finishdate      = DateTimeField()
    folderreference = StringField(default="")
    meta            = {'allow_inheritance': True}
    tasks           = ListField(ReferenceField(Task), required=False)
    
    def getShortDescription(self):
        return (self.description[:130] + " ...") if(len(self.description)>130) else self.description
    

    def taskCount(self):
        return(len(self.tasks))

    def getEndPercent(self):

        realpercent     =0
        for task in self.tasks:
            realpercent = realpercent + int(task.endpercent)
        totalpercent    = len(self.tasks) * 100
        return (0) if(realpercent <= 0) else round((float(float(100)/ float(totalpercent))) * float(realpercent))
        
    def daysLeft(self):
        if(self.finished == False):
            realdifference  = self.dateend.date() -datetime.datetime.now().date()
            return realdifference.days
        else:
            realdifference  = self.dateend -datetime.datetime.now()
            return  0


    
    
    
class Taskstatus(Document):
    name            = StringField(max_length=2000)
    meta            = {'allow_inheritance': True}


class driveConfiguration(Document):

    active          = BooleanField(default=True)
    datestart       = DateTimeField(default=datetime.datetime.now)
    token           = StringField()
    credential      = StringField()



class KnowledgeTips(Document):
    
    reference       = StringField(default="")
    referencetype   = StringField(default="task")
    description     = StringField()
    title           = StringField()
    keywords        = ListField()
    owner           = ReferenceField(User)
    active          = BooleanField(default= True)
    dateadd         = DateTimeField(default=datetime.datetime.now)
    



    
    
    
    


    
    

