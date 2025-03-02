from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.

@api_view(['POST'])
def CreateUser(request):
    data=json.loads(request)
    print(data)
    return Response({"message":"here i am "},status=200)