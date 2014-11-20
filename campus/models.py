from django.db import models

# Create your models here.
class Lecturer(models.Model) :
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    @property
    def full_name(self):
        return "%s %s" % (self.name, self.surname)

    def __unicode__(self): 
        return "%s %s" % (self.name, self.surname)

    class Meta:
        unique_together = ('name', 'surname',)

    