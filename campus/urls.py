from django.conf.urls import url

from campus import views

urlpatterns = [
   url(r'^$', views.message_lecturer, name='message_lecturer'),
   url(r'^$', views.admin_table, name='lecturers'),
]