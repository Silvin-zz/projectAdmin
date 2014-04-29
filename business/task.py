
__author__ = 'bravocado'
from principal.models import Task
class BTask(Task):
    def getAll(self, active=True):
        return Task.objects.filter(active =active)
        
        
    def saveProgress(self, parameters):
        localTask                =Task.objects.get(id=parameters["taskid"])
        localTask.occupiedhours  =parameters["occupiedhours"]
        localTask.endpercent     =parameters["endpercent"]
        localTask.save()
        return (True)