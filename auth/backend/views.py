from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import json


@api_view(["POST"])
def CreateUser(request):
    try:
        data = request.data

        id = data.get("username")
        pwd = data.get("password")
        # get data
        data = request.data

        # extract id and password
        id = data.get("username")
        pwd = data.get("password")

        # handle if either one is not provided
        if not id or not pwd:
            return Response(
                {"error": "Username or password is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # check if user already exist
        if User.objects.filter(username=id).exists():
            return Response(
                {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(username=id, password=pwd)

        return Response(
            {"messsage": "User successfully created"}, status=status.HTTP_201_CREATED
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def LoginUser(request):
    try:
        data = request.data

        id = data.get("username")
        pwd = data.get("password")

        if not id or not pwd:
            return Response(
                {"message": "id and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=id, password=pwd)
        print(user)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    "message": "Login Successfull",
                    "access_token": access_token,
                    "refresh_token": str(refresh),
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
    except json.JSONDecodeError:
        return Response(
            {"message": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def secure_page(request):
    user=request.user
    return Response({"message":f"Hello {user}, you are authenticated"})