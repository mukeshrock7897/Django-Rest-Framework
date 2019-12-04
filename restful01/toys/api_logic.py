from django.urls import path
from toys.serializers import ToySerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http import HttpResponse , JsonResponse , Http404
from rest_framework.decorators import api_view
from rest_framework.renderers import BrowsableAPIRenderer


from toys.models import Toy

@csrf_exempt
@api_view(["GET","POST"])
def create_toy(request):
    if request.method == "GET":
        employees = Toy.objects.all()
        serializer = ToySerializer(employees , many=True)
        if employees.count()==0:
            return HttpResponse("No Record Found in Database")
        return JsonResponse(serializer.data,status=200,safe=False)
        

    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializer = ToySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages  , status=404)


@csrf_exempt
@api_view(["GET","PUT","DELETE","PATCH"])
def detail_toy(request,id):
    try:
        toy = Toy.objects.get(pk=id)
    except Toy.DoesNotExist:
        return HttpResponse("Not Found Any Toy with this ID")

    if request.method == "GET":
        serializer = ToySerializer(toy)
        return JsonResponse(serializer.data  , safe=False)
        

    elif request.method=="PUT":
        toy_data = JSONParser().parse(request)
        serializer = ToySerializer(toy,data=toy_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages  , status=404)

    elif request.method=="PATCH":
            
        toy_data = JSONParser().parse(request)
        serializer = ToySerializer(toy,data=toy_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages  , status=404)

    elif request.method=="DELETE":
        toy.delete()
        return HttpResponse(status=404)

