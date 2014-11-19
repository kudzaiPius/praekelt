from django.db import models

# Create your models here.
class Lecturer(models.Model) :
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)

	def _full_name(self):
        	return "%s %s" % (self.name, self.surname)

    	full_name = property(_full_name)