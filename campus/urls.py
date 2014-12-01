from django.conf.urls import url

from campus import views

urlpatterns = [
   url(r'^$', views.messageLecturer, name='messageLecturer'),
   url(r'^$', views.adminTable, name='adminTable'),
]