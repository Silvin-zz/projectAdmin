__author__ = 'silvio.bravo'
from principal.models import Project
class BProject(Project):
    def getAllProjects(self, active=True):
        return Project.objects.filter(active =active)
