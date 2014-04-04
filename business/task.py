__author__ = 'bravocado'
from principal.models import Task
class BTask(Task):
    def getAll(self, active=True):
        return Task.objects.filter(active =active)
