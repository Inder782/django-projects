from django.contrib import admin
from django.urls import path
from backend.views import CreateUser,LoginUser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("backend/register",CreateUser,name="register"),
    path("backend/login",LoginUser,name="login"),

