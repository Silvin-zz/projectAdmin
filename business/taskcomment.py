__author__ = 'temporal'
from principal.models import Taskcomment
from principal.models import AuthUser
from principal.models import Task
from principal.models import Taskstatus

class BTaskComment(Taskcomment):
    
    def getAll(self, taskId):
        return Taskcomment.objects.filter(taskid=taskId)
        
        
    def addComment(self, userid, taskid, txtComment):
        
        taskObject                  = Task.objects.get(id=taskid);
        commentObject               = Taskcomment(
                                            taskid      = taskObject,
                                            owner       = AuthUser.objects.get(id=userid),
                                            taskstatus  = taskObject.statusid,
                                            comment     = txtComment,
                                            dateadd     = '2014-04-07'
                                            
                                        );
        
        commentObject.save()
        
        return (commentObject)
        
