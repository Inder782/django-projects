from sqlite3 import IntegrityError
from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.models import User

#read all tasks
def task_list(request):
    tasks= Task.objects.all()
    return render(request,"task/task_list.html",{'tasks':tasks})

#create a task
def add_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description= request.POST.get('description')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')

#delete task
def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('task_list')
