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


class Company(Document):
    name        = StringField(max_length=500, required=True)
    description = StringField(max_length=2000)


class Taskcomment(Document):
    comment     = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
class AuthUser(Document):
    first_name  = StringField(max_length=2000)
    meta = {'allow_inheritance': True}


class Task (Document):
    title   = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
    
class Taskstatus(Document):
    name    = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
    
class Project(Document):
    title    = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
    
class Projecttype(Document):
    name    = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
    
class Client(Document):
    name    = StringField(max_length=2000)
    meta = {'allow_inheritance': True}
    
class User(Document):
    name    = StringField(max_length=2000)
    

