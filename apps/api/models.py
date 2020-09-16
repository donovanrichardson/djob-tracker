from django.db import models
from ..authentication.models import User


class Location(models.Model):

    name = models.CharField(max_length=255, primary_key=True)
    rating = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Job(models.Model):

    title = models.TextField()
    company = models.CharField(max_length=255)
    description = models.TextField(default='')
    keywords = models.CharField(max_length=255, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

