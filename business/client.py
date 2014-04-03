__author__ = 'temporal'
from principal.models import Client
class BClient(Client):
    def getAll(self, active=True):

        return Client.objects.all()
