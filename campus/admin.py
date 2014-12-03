from django import forms
from django.contrib import admin
from django.core import validators
from django.core.exceptions import ValidationError

from campus import forms
from campus.models import Lecturer

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'full_name') 