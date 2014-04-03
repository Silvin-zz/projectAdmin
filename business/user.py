__author__ = 'temporal'
from principal.models import AuthUser
class BUser(AuthUser):
    def getAllProjects(self, active=True):
        return AuthUser.objects.all()
