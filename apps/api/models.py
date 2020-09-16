from django.db import models
from ..authentication.models import User


class Location(models.Model):

    name = models.CharField(max_length=255, primary_key=True)
    rating = models.IntegerField(default=0, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Job(models.Model):

    title = models.TextField()
    company = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    keywords = models.CharField(max_length=255, blank=True, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField()
    rating = models.IntegerField(default=0, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

