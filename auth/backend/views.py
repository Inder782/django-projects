from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import json

@api_view(['POST'])
def simple_function(request):
    try:
        data=request.data
        
        id=data.get('username')
        pwd= data.get('password')

        if not id or not pwd:
            return Response({"error":"Username or password is required"},status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=id).exists():
            return Response({"error":"User already exists"},status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(username=id,password=pwd)

        return Response({"messsage":"User successfully created"},status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)