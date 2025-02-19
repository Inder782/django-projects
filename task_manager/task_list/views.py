from django.shortcuts import render,redirect
from .models import Task
# Create your views here.

def task_list(request):
    tasks= Task.objects.all()
    return render(request,"task/task_list.html",{'tasks':tasks})

def add_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description= request.POST.get('description')
        if title:
            Task.objects.create(title=title)
            Task.objects.create(description=description)
            return redirect('task_list')