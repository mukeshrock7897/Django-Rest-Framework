
from django.urls  import path
from drones import views


urlpatterns = [
    path("drone-catrgories/",views.DroneCategoryList.as_view() , name=views.DroneCategoryList.name),
    path("drone-catrgories/<int:pk>",views.DroneCategoryDetail.as_view() , name=views.DroneCategoryDetail.name),
    path("drones/",views.DroneList.as_view() , name=views.DroneList.name),
    path("drones/<int:pk>",views.DroneDetail.as_view() , name=views.DroneDetail.name),
    path("piolts/",views.PioltList.as_view() , name=views.PioltList.name),
    path("piolts/<int:pk>",views.PioltDetail.as_view() , name=views.PioltDetail.name),
    path("competitions/",views.CompetitionList.as_view() , name=views.CompetitionList.name),    
    path("competitions/<int:pk>",views.CompetitionDetail.as_view() , name=views.CompetitionDetail.name),
    path("",views.ApiRoot.as_view(),name=views.ApiRoot.name)    


]