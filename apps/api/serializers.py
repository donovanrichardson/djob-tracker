from .models import Job, Location
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id","title", "company","description","keywords","location", "url","user", "rating")

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("name", "rating","user")
