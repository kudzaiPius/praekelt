from django.contrib import admin
from .models import Lecturer

class LecturerAdmin(admin.ModelAdmin):
    #fields = ('name', 'surname')
    list_display = ('name', 'surname', 'full_name')
    #ordering = ['full_name']#['name', 'surname']

# Register your models here.
admin.site.register(Lecturer, LecturerAdmin)