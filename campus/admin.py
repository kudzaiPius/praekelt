from django.contrib import admin
from .models import Lecturer


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'full_name')

admin.site.register(Lecturer, LecturerAdmin)