from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.


class DroneCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:

        ordering = ("name",)
    
    def __str__(self):
        return self.name


class Drone(models.Model):

    name = models.CharField(max_length=100 , unique=True)
    drone_category = models.ForeignKey(DroneCategory , on_delete=models.CASCADE)
    manufacturing_date  = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User' , related_name='drones' , on_delete=models.CASCADE,null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Piolt(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gender_choice = (
        ("Male","Male"),
        ("Female","Female")
    )

    gender = models.CharField(max_length=100 , choices=gender_choice)
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name

class Competition(models.Model):

    piolt = models.ForeignKey(Piolt,on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone,on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateField()


    class Meta:
        ordering = ("-distance_in_feet",)

    def __str__(self):
        return self.name
        
