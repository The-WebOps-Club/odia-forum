from django.db import models
from pybb.models import Topic
# Create your models here.

# semantically, topic should contain a many to many field topic, but since we're trying not to disturb pybb's files, we implement it in a reverse fashion
class Tag(models.Model):
	topics = models.ManyToManyField(Topic)
	label = models.CharField( max_length=30 )
	desc = models.CharField( max_length = 200)