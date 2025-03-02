from django.contrib import admin
from django.urls import path
from backend.views import CreateUser
urlpatterns = [
    path("admin/", admin.site.urls),
    path("backend/register",CreateUser,name="register")
]
