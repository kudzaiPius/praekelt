from django.db import models
from campus import customfields
from campus.validators import validate_name, validate_over_18
import datetime

class Lecturer(models.Model) :
    name = models.CharField(max_length=200, validators=[validate_name])
    surname = models.CharField(max_length=200, validators=[validate_name])
    date_of_birth = models.DateField('date_of_birth', default=datetime.date.today, validators=[validate_over_18])

    @property
    def full_name(self):
        return "%s %s" % (self.name, self.surname)

    def __unicode__(self): 
        return "%s %s" % (self.name, self.surname)

    class Meta:
        unique_together = ('name', 'surname',)