from django.contrib import admin
from .models import Lecturer


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'full_name')

admin.site.register(Lecturer, LecturerAdmin)