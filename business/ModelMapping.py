import datetime
import json

class ModelMapping:
    def targetMapping(self, targets):
        result=[]
        for target in targets:
            result.append({
                "id"            : str(target.id), 
                "title"         : target.title, 
                "description"   : target.description, 
                "shortdesc"     : target.getShortDescription(), 
                "tasksNumber"   : target.taskCount(), 
                "endPercent"    : target.getEndPercent(),
                "datestart"     : str(target.datestart.date()),
                "dateend"       : str(target.dateend.date()), 
                "code"          : target.code,
                "targettype"    : str(target.targettype.id),
                "finished"      : target.finished,
                "owner"         : {
                                    "name"      : target.owner.name,
                                    "img"       : "/static/images/users/" + str(target.owner.getUrlImage()),
                                    "id"        : str(target.owner.id)
                                }
                })
        return result


    def taskMapping(self, tasks):
        result=[]
        for task in tasks:
            result.append({
                "id"            : str(task.id), 
                "title"         : task.title, 
                "description"   : task.description, 
                "shortdesc"     : task.getShortDescription(), 
                "code"          : task.code,
                "tasktype"      : str(task.tasktype.id), 
                "priority"      : str(task.priority.id), 
                "iscritical"    : str(task.iscritical),
                "dateend"       : str(task.dateend.date()), 
                "datestart"     : str(task.datestart.date()), 
                "finished"      : task.finished,
                "estimatedhours": task.estimatedhours,
                "endpercent"    : task.endpercent,
                "owner"         : {
                                    "name"      : task.owner.name,
                                    "img"       : "/static/images/users/" + str(task.owner.getUrlImage()),
                                    "id"        : str(task.owner.id)
                                }
                })
        return result
        
    def catalogMapping(self, data):
        result= []
        for objectCatalog in data:
            result.append({
                "id"            : str(objectCatalog.id), 
                "name"          : objectCatalog.name
                
                })
        return result
        
        
    
        
        
    
    def dayByDayMapping(self, data):
        result= []
        projectId  = None
        editable   = True
        isUsed     = False
        
        for dayObject in data:
            
            editable   = True
            isUsed     = False
            
            
            editable   = not dayObject.isCalendar
            if dayObject.isCalendar == True:
                if datetime.datetime.now() > dayObject.dateend:
                    isUsed   = True
                    editable = True
            
            
            projectId  = None;
            if hasattr(dayObject, 'project'):
                if hasattr(dayObject.project, "id"):
                    projectId = str(dayObject.project.id)
                
            result.append({
                "id"                : str(dayObject.id), 
                "title"             : dayObject.title,
                "description"       : dayObject.description,
                "start"             : dayObject.datestart.strftime("%Y-%m-%dT%H:%M:%S"),
                "end"               : dayObject.dateend.strftime("%Y-%m-%dT%H:%M:%S"),
                "activity"          : str(dayObject.activity.name),
                "borderColor"       : "#" + str(dayObject.activity.color),
                "backgroundColor"   : "#" + str(dayObject.activity.color),
                "activity"          : str(dayObject.activity.id),
                "allDay"            : False,
                "projectId"         : projectId,
                "editable"          : editable,
                "isCalendar"        : dayObject.isCalendar,
                "isUsed"            : isUsed,
                })
        return result




    def userMapping(self, data):
        area = ""
        areaid= None
        result= []
        for objectCatalog in data:
            
            if objectCatalog.area == None:
                area= None
                areaid=None
            else:
                area   = objectCatalog.area.name
                areaid = str(objectCatalog.area.id)
            result.append({
                "id"            : str(objectCatalog.id), 
                "name"          : objectCatalog.name,
                "profile"       : objectCatalog.profile.name,
                "profileid"     : str(objectCatalog.profile.id),
                "area"          : area,
                "email"         : objectCatalog.email,
                "username"      : objectCatalog.username,
                "image"         : objectCatalog.getUrlImage(),
                "areaid"        : areaid,
                
                })
        return result
    

    def genericMapping(self, data):
        area = ""
        result= []
        for objectCatalog in data:
            
            
            result.append({
                "id"            : str(objectCatalog.id), 
                "name"          : objectCatalog.name,
                
                })
        return result
    

