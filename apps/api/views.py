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
        print(data)
        print(data.get('keywords'),'')
        job_inst = Job(
            title = data['title'],
            company = data['company'],
            url = data['url'],
            keywords = data.get('keywords') if data.get('keywords') else '',
            description= data['description'],
            rating=data.get('rating',0),
            user_id = request.user.id,
        )
        # print(job_inst.keywords)
        # print(job_inst)

        try:
            loc_inst = Location.objects.get(pk=data['location_id'])
        except(Location.DoesNotExist):
            loc_inst = Location.objects.create(name=data['location_id'], user_id = request.user.id)
            loc_inst.save()

        job_inst.location_id = data['location_id']
        # print()
        # print(data)
        job_inst.save()
        serialized = JobSerializer(job_inst)
        return Response(serialized.data)

    def partial_update(self, request, *args, **kwargs):
        print('***partial_update is called***')
        job_instance = self.get_object()
        if job_instance.user_id != request.user.id:
            return Response({
                "message": "you are not authorized to modify this Job record"
            })
        job_instance.title = request.data.get('title', job_instance.title)
        job_instance.description = request.data.get('description', job_instance.description)
        job_instance.company = request.data.get('company', job_instance.company)
        job_instance.url = request.data.get('url', job_instance.url)
        job_instance.keywords = request.data.get('keywords', job_instance.keywords)
        job_instance.rating=data.get('rating',job_instance.rating)
        job_instance.save()
        serializer = JobSerializer(job_instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        the_jobs = Job.objects.filter(user_id = request.user.id)
        serialized = JobSerializer(the_jobs, many=True)
        return Response(serialized.data)

    def destroy(self, request, *args, **kwargs):
        job_inst = self.get_object()
        if job_inst.user_id != request.user.id:
            return Response({
                "message": "you are not authorized to delete this Job record"
            })
        job_inst.delete()
        serializer = JobSerializer(job_inst)
        return Response({
            'message': 'record deleted',
            'record': serializer.data
        })

#         Location.objects.get(pk="whatever") except apps.api.models.Location.DoesNotExist: as none, if none, add, otherwise add this loc to the job inst.

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        the_locations = Location.objects.filter(user_id = request.user.id)
        serialized = LocationSerializer(the_locations, many=True)
        return Response(serialized.data)

    def partial_update(self, request, *args, **kwargs):
        print('***partial_update is called***')
        location_instance = self.get_object()
        if location_instance.user_id != request.user.id:
            return Response({
                "message": "you are not authorized to modify this Location record"
            })
        location_instance.name = request.data.get('name', location_instance.name)
        location_instance.rating = request.data.get('rating', location_instance.rating)
        location_instance.save()
        serializer = LocationSerializer(location_instance)
        return Response(serializer.data)

# Todo if self.get_object is not an object, like the id is incorrect
    def destroy(self, request, *args, **kwargs):
        loc_inst = self.get_object()
        if loc_inst.user_id != request.user.id:
            return Response({
                "message": "you are not authorized to delete this Location record"
            })
        loc_inst.delete()
        serializer = LocationSerializer(loc_inst)
        return Response({
            'message': 'record deleted',
            'record': serializer.data
        })

