from django.contrib import admin
from django.urls import path
from backend.views import simple_function
urlpatterns = [
    path("admin/", admin.site.urls),
    path("backend/register",simple_function,name="register")
]
