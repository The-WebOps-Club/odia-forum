from django.db import models
from accounts.models import UserData,institutes

class Event(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=100)
	date_time = models.DateTimeField('Date, time')
	location = models.CharField(max_length=40)
	users = models.ManyToManyField(UserData)
	
	def __unicode__(self):
		return self.name
	

class Update(models.Model):
	title = models.CharField(max_length=30)
	date_time = models.DateTimeField('Date, time')
	update = models.TextField(max_length=50)
	
	def __unicode__(self):
		return self.title
		
class Homepage(models.Model):
	institute = models.CharField(choices = institutes, max_length=50)
	description = models.TextField(max_length=200)
	image = models.ImageField(upload_to='media/homepages/')
	
	def __unicode__(self):
		return self.institute