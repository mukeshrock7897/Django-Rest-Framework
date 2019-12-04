from django.contrib import admin
from toys.models import Toy


class ToyAdmin(admin.ModelAdmin):
    list_display=("name" , "toy_category" ,"created" ,"release_date")
    readonly_fields = ('created',"release_date")


admin.site.register(Toy,ToyAdmin)


