__author__ = '@silvio.bravo'
from principal.models import Menu
from principal.models import AuthGroup
from principal.models import AuthUser
from principal.models import AuthUserGroups;
from principal.models import Groupmenu
class BMenu(Menu):
    def getOptions(self, userObject):

        usergroups  = AuthUserGroups.objects.filter(user_id=userObject.id)
        groupmenu   = Groupmenu.objects.filter(groupid=usergroups[0].group_id)
        menus       =[]
        for aux in groupmenu:
            menus.append(aux.menuid)
        return menus




