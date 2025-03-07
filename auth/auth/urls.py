from django.contrib import admin
from django.urls import path
from backend.views import CreateUser,LoginUser,secure_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("backend/register",CreateUser,name="register"),
    path("backend/login",LoginUser,name="login"),
    path("secure",secure_page,name="secure_point")
]

