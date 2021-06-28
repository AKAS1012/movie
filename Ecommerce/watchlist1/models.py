from django.db import models


# Create your models here.
class StreamPlatform(models.Model):
	name = models.CharField(max_length=30)
	about = models.CharField(max_length=150)
	website = models.URLField(max_length=100)

	def __str__(self):
		return self.name


class Watchlist(models.Model):
	title = models.CharField(max_length=50)
	storyline = models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	created = models.DateTimeField()

	def __str__(self):
		return self.title
