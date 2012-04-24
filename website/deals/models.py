from django.db import models

class Site(models.Model);
	site_name = models.CharField(max_length=20)

class Deal(models.Model):
	site = ForeignKey(Site)
	title = models.CharField(max_length=1000)
	begin_date = models.DateTimeField()
	end_date = models.DateTimeField()
	def __unicode__(self):
		return self.title


# Create your models here.
