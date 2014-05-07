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

import os.path


class Company(Document):
    name        = StringField(max_length=500, required=True)
    description = StringField(max_length=2000)


class Taskcomment(Document):
    comment     = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
class AuthUser(Document):
    first_name  = StringField(max_length=2000)
    meta = {'allow_inheritance': True}










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
    meta            = {'allow_inheritance': True}



class Profile(Document):
    name           = StringField()
    options        = ListField(ReferenceField(Menu))
    meta           = {'allow_inheritance': True}




class User(Document):

    name            = StringField(max_length=2000)
    username        = StringField(max_length=2000)
    password        = StringField()
    profile         = ReferenceField(Profile)
    active          = BooleanField()
    email           = EmailField()
    meta            = {'allow_inheritance': True}
    
    def getUrlImage(self):
        return ("1.png")


#Terminamos el manejo de usuarios.




    
class Projecttype(Document):
    name            = StringField(max_length=2000)
    active          = BooleanField()
    meta            = {'allow_inheritance': True}





class Project(Document):

    title           = StringField(max_length=2000)
    description     = StringField()
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
    totaltasks      = IntField(default=0)
    totalendtask    = IntField(default=0)
    advancepercent  = DecimalField(default=0)
    priority        = IntField(default=1)
    meta            = {'allow_inheritance': True}

    
    def dateDiff(self):
        difference = self.dateend - self.datestart
        return difference.days

    def timePercent(self):
        difference =  datetime.now() - self.datestart
        return round((Decimal(100) / Decimal(self.dateDiff())) * difference.days,2)

    def endPercent(self):
        if(self.totaltasks >0):
            return  round((Decimal(100) / Decimal(self.totaltasks)) * self.totalendtask,2)
        return 0



    meta = {'allow_inheritance': True}    
    



class Comment(EmbeddedDocument):
    description     = StringField()
    date            = DateTimeField()
    user            = ReferenceField(User)



class Stage(Document):
    name            = StringField()


class TaskType(Document):
    name            = StringField()






class Task (EmbeddedDocument):
    title           = StringField(max_length=2000)
    description     = StringField()
    active          = BooleanField(default=True)
    project         = ReferenceField(Project)
    owner           = ReferenceField(User)
    comments        = ListField(EmbeddedDocumentField(Comment))
    datestart       = DateTimeField()
    dateend         = DateTimeField()
    realdatestart   = DateTimeField()
    realdateend     = DateTimeField()
    dateadd         = DateTimeField()
    tasktype        = ReferenceField(TaskType)
    endpercent      = IntField(default=0)
    estimatedhours  = IntField(default=0)
    usedhours       = IntField(default=0)
    iscritical      = BooleanField(default= False)
    finished        = BooleanField(default= False)
    meta            = {'allow_inheritance': True}



class Target(Document):
    title           = StringField(max_length=2000)
    description     = StringField()
    owner           = ReferenceField(User)
    project         = ReferenceField(Project)
    datestart       = DateTimeField()
    dateend         = DateTimeField()
    realdatestart   = DateTimeField()
    realdateend     = DateTimeField()
    endpercent      = IntField(default=0)
    comments        = ListField(EmbeddedDocumentField(Task))
    finished        = BooleanField(default = False)
    meta            = {'allow_inheritance': True}

    
    
    
class Taskstatus(Document):
    name            = StringField(max_length=2000)
    meta            = {'allow_inheritance': True}

    
    

