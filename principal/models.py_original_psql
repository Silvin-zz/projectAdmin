# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    rfc = models.TextField(blank=True)
    city = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    email = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'client'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    size = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    url = models.TextField(blank=True)
    extension = models.TextField(blank=True)
    contenttype = models.TextField(blank=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    useradd = models.ForeignKey(AuthUser, db_column='useradd')
    taskid = models.ForeignKey('Task', db_column='taskid', blank=True, null=True)
    projectid = models.ForeignKey('Project', db_column='projectid', blank=True, null=True)
    documenttypeid = models.ForeignKey('Documenttype', db_column='documenttypeid', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'document'

class Documenttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    forproject = models.NullBooleanField()
    fortask = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'documenttype'

class Groupmenu(models.Model):
    id = models.IntegerField(primary_key=True)
    groupid = models.ForeignKey(AuthGroup, db_column='groupid')
    menuid = models.ForeignKey('Menu', db_column='menuid')
    class Meta:
        managed = False
        db_table = 'groupmenu'

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'menu'

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    clientid = models.ForeignKey(Client, db_column='clientid')
    datestart = models.DateField()
    dateend = models.DateField()
    owner = models.ForeignKey(AuthUser, db_column='owner')
    projecttypeid = models.ForeignKey('Projecttype', db_column='projecttypeid')
    inuse = models.NullBooleanField(default=True)
    active = models.NullBooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'project'

class Projectpatner(models.Model):
    id = models.IntegerField(primary_key=True)
    projectid = models.ForeignKey(Project, db_column='projectid')
    userid = models.ForeignKey(AuthUser, db_column='userid')
    class Meta:
        managed = False
        db_table = 'projectpatner'

class Projecttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    active = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'projecttype'

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    datestart = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    realdatestart = models.DateTimeField(blank=True, null=True)
    realdateend = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    priority = models.IntegerField(blank=True, null=True)
    ownerid = models.ForeignKey(AuthUser, db_column='ownerid', related_name='owner', blank=True, null=True)
    projectid = models.ForeignKey(Project, db_column='projectid')
    typeid = models.ForeignKey('Tasktype', db_column='typeid')
    estimatedhours = models.IntegerField(blank=True, null=True)
    occupiedhours = models.IntegerField(blank=True, null=True)
    statusid = models.ForeignKey('Taskstatus', db_column='statusid')
    finished = models.NullBooleanField()
    active = models.NullBooleanField()
    dateadd = models.DateTimeField(blank=True, null=True)
    datemodified = models.DateTimeField(blank=True, null=True)
    useradd = models.ForeignKey(AuthUser, db_column='useradd', related_name='useradded', blank=True, null=True)
    usermodified = models.ForeignKey(AuthUser, db_column='usermodified', blank=True, null=True)
    endpercent = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'task'

class Taskcomment(models.Model):
    id = models.AutoField(primary_key=True)
    taskid = models.ForeignKey(Task, db_column='taskid', blank=True, null=True)
    owner = models.ForeignKey(AuthUser, db_column='owner', blank=True, null=True)
    taskstatus = models.ForeignKey('Taskstatus', db_column='taskstatus', blank=True, null=True)
    comment = models.TextField(blank=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'taskcomment'

class Taskflow(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.ForeignKey(Task, db_column='taskid', blank=True, null=True)
    taskstatusid = models.ForeignKey('Taskstatus', db_column='taskstatusid', blank=True, null=True)
    dateadd = models.DateTimeField(blank=True, null=True)
    useradd = models.ForeignKey(AuthUser, db_column='useradd', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'taskflow'

class Taskstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'taskstatus'

class Tasktype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tasktype'

