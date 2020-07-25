from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mathtestapi.models import Users
from mathtestapi.serializers import UsersSerializer
# Create your views here.
@csrf_exempt
def user_list(request):
    
    #List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    #Retrieve, update or delete a code snippet.
    try:
        users = Users.objects.get(pk=pk)
    except mathtestapi.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(users)
        serializer = UsersSerializer(users, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def login(request, pk=None):
    #Retrieve, update or delete a code snippet.
    #post_data = request.data
    #print(post_data)
    return Response(data="return data")
