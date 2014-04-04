__author__ = 'silvio.bravo'
from principal.models import Projecttype
class BProjectType(Projecttype):
    def getAllProjects(self, active=True):
        return Projecttype.objects.filter(active =active)
