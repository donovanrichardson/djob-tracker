from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=255, primary_key=True)
    rating = models.IntegerField(null=True)

class Job(models.Model):

    title = models.TextField()
    company = models.CharField(max_length=255)
    description = models.TextField(default='')
    keywords = models.CharField(max_length=255, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.URLField()

