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

    url(r'^tasks/list','principal.views.tasksList'),
    url(r'^tasks/admin','principal.views.tasksAdmin'),

    url(r'^teams/list','principal.views.teamList'),
    url(r'^documents/list','principal.views.documentList'),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
