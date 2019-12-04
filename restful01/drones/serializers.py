from rest_framework import serializers 
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Piolt
from drones.models import Competition

class DroneCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = DroneCategory
        fields = "__all__"


class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = "__all__"


class PioltSerializer(serializers.ModelSerializer):

    class Meta:
        model = Piolt
        fields = "__all__"


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields= "__all__"

        