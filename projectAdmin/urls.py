from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectAdmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','login.views.home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/validate/','login.views.userValidate'),
    url(r'^dashboard/','principal.views.index'),


    ##############PROJECTS#########################


    url(r'^projects/list','principal.project.projectList'),
    url(r'^projects/new','principal.project.projectAdd'),
    url(r'^projects/edit','principal.project.projectEdit'),
    url(r'^projects/delete','principal.project.projectDelete'),
    url(r'^projects/save','principal.project.projectSave'),


    ##############TASKS#########################

    url(r'^tasks/list'          ,'principal.task.taskList'),
    url(r'^tasks/new'           ,'principal.task.taskAdd'),
    url(r'^tasks/show'          ,'principal.task.showDetail'),
    url(r'^tasks/admin'         ,'principal.task.taskAdmin'),
    url(r'^tasks/savetimeline'  ,'principal.task.saveTimeLine'),
    url(r'^tasks/save'          ,'principal.task.taskSave'),
    url(r'^tasks/mytasks'       ,'principal.task.myTasks'),
    
    

    #######################DOCUMENTS, WITH GOOGLE SOURE#########################

    url(r'^document/show'          ,'principal.document.showDocuments'),
    url(r'^document/getList'       ,'principal.document.getList'),
    url(r'^document/newFolder'     ,'principal.document.newFolder'),
    
    

    


    ##############TARGETS #########################

    url(r'^target/list','principal.target.targetList'),
    url(r'^target/getbyproject','principal.target.getTargetByProjectId'),
    url(r'^target/save','principal.target.targetSave'),
    url(r'^target/detail','principal.target.targetDetail'),
    url(r'^target/prueba','principal.target.targetPrueba'),
    

     ##############COMMENTS#########################

    url(r'^comment/addfortask','principal.comment.addForTask'),
    url(r'^comment/list','principal.comment.listByTaskId'),


    url(r'^teams/list','principal.views.teamList'),
    url(r'^documents/list','principal.views.documentList'),


    ####################CLIENT ###########################
    url(r'^client/save-ajax','principal.client.saveNewByAjax'),



) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
