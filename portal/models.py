from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=60)
	date_time = models.DateTimeField('Event date + time')
	location = models.CharField(max_length=40)
	
	def __unicode__(self):
		return self.name
	

class Update(models.Model):
	title = models.CharField(max_length=30)
	date_time = models.DateTimeField('Update date + time')
	update = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.title
		
