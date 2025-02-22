
from django.contrib import admin
from django.urls import path
from api.views import create_tasks,get_tasks,delete_task

urlpatterns = [
    path("create",create_tasks,name="create_task"),
    path("all/",get_tasks,name="all_tasks"),
    path("delete/<int:task_id>",delete_task,name="delete_tasks"),
    path("update/<int:task_id>",delete_task,name="update_task")
]
