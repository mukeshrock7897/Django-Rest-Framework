from django.shortcuts import render

from drones.models import DroneCategory 
from drones.models import Drone
from drones.models import Piolt
from drones.models import Competition

from drones.serializers import DroneCategorySerializer
from drones.serializers import DroneSerializer
from drones.serializers import PioltSerializer
from drones.serializers import CompetitionSerializer

from rest_framework.response import Response
from rest_framework.reverse  import reverse
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle





class DroneCategoryList(generics.ListCreateAPIView):

    queryset  = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"



class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset  = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-detail"


class DroneList(generics.ListCreateAPIView):

    queryset= Drone.objects.all()
    serializer_class = DroneSerializer
    name  ="drone-list"
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes  = (

        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
    )

    
    def perform_create(self , serializer):
        serializer.save(owner=self.request.user)

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):

    throttle_scope ='drones'
    throttle_classes  = [ScopedRateThrottle]
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"

class PioltList(generics.ListCreateAPIView):

    queryset = Piolt.objects.all()
    serializer_class = PioltSerializer
    name = "piolt-list"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class PioltDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Piolt.objects.all()
    serializer_class = PioltSerializer
    name = "piolt-detail"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CompetitionList(generics.ListCreateAPIView):

    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = "competition-list"

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = "competition-detail"




class ApiRoot(generics.GenericAPIView):
    
    name = "api-root"
    def get(self , request , *agrs , **kwrgs):

        return Response(
            {
            'drone-categories':reverse(DroneCategoryList.name , request=request),
            'drones':reverse(DroneList.name , request=request),
            'piolts':reverse(PioltList.name , request=request),
            'competitions':reverse(CompetitionList.name , request=request)            
            }
                )
