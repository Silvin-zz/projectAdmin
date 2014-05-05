__author__ = 'temporal'
from principal.models import User
class BUser(User):
    def getAllProjects(self, active=True):
        return User.objects.all()
