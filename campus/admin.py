from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Lecturer
from campus import forms

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    form = forms.customAdminForm