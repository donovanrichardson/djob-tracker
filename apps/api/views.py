from django.shortcuts import render
from .models import Job, Location
from rest_framework import viewsets, permissions
from .serializers import JobSerializer, LocationSerializer
from rest_framework.response import Response

class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('*  cre8 iz kawld  *')
        # print(request.data)
        data = request.data
        job_inst = Job(
            title = data['title'],
            company = data['company'],
            url = data['url'],
            keywords = data['keywords'],
            description= data['description']
        )
        print(job_inst)

        try:
            loc_inst = Location.objects.get(pk=data['location_id'])
        except(Location.DoesNotExist):
            loc_inst = Location.objects.create(name=data['location_id'])
            loc_inst.save()

        job_inst.location_id = data['location_id']
        # print()
        # print(data)
        job_inst.save()
        serialized = JobSerializer(job_inst)
        return Response(serialized.data)


#         Location.objects.get(pk="whatever") except apps.api.models.Location.DoesNotExist: as none, if none, add, otherwise add this loc to the job inst.

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

