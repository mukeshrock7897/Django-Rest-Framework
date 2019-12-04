
from toys.api_logic import create_toy , detail_toy
from django.urls  import path


urlpatterns = [
    path("create/",create_toy),
    path("create/<int:id>",detail_toy),
]