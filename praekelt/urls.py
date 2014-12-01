from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'praekelt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lecturers/$', 'campus.views.adminTable', name='lecturers'),
    url(r'^message-Lecturer/$', 'campus.views.messageLecturer', name='messageLecturer'),
    url(r'^messageLecturer/$', 'campus.views.messageLecturer', name='messagePOST'),
)
