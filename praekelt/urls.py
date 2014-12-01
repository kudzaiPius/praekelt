from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'praekelt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/campus/lecturers/$', 'campus.views.adminTable', name='lecturers'),
    url(r'^admin/campus/message-Lecturer/$', 'campus.views.messageLecturer', name='messageLecturer'),
    url(r'^admin/', include(admin.site.urls)),
)
