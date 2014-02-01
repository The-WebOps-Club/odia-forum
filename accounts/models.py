from django.db import models
from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User


class UserData(models.Model):
	user = models.OneToOneField(User)
	
	address = models.CharField(max_length=200)
	institute = models.CharField(max_length=50)
	hostel_bool = models.BooleanField(default=False)
	hostel = models.CharField(max_length=40)
	department = models.CharField(max_length=40)
	
	# Soft code the next line ASAP.
	# batchof = models.ChoiceField(choices = make_str(range(1955,datetime.datetime.now().year+1)))
	batchof = models.CharField(max_length=10)
	graduation_date = models.DateField(auto_now=True)
	course = models.CharField(max_length=100)