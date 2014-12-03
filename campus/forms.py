from django import forms
from .models import Lecturer
import datetime
from django.core.exceptions import ValidationError

class customAdminForm(forms.ModelForm):

    class Meta:
        model = Lecturer

class messageLecturerForm(forms.Form):
    lecturers = forms.ChoiceField(label=u'Lecturer', required=True)
    message_text = forms.CharField(widget=forms.Textarea, required=True, 
    	max_length=1500)
    
    def is_valid(self):
    	valid = super(messageLecturerForm, self).is_valid()

    	if not valid:
    		return valid