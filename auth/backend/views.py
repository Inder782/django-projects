from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# Create your views here.

@api_view(['POST'])
def simple_function(request):
    data= json.loads(request.body)
    print(data)
    data={"message":" love from backend"}
    return Response(data,status=200)