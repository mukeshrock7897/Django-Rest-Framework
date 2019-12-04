from django.contrib import admin
from drones.models import DroneCategory , Drone , Piolt ,Competition


# Register your models here.


admin.site.register(DroneCategory)
admin.site.register(Drone)
admin.site.register(Piolt)
admin.site.register(Competition)