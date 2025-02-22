from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(["GET"])
def get_tasks(request):
    tasks=Task.objects.all()
    response=TaskSerializer(tasks,many=True)
    return Response(response.data,status=200)

@api_view(['POST'])
def create_tasks(request):
    data=request.GET.get('title')
    task=Task.objects.create(title=data)
    task.save()
    return Response(status=200)

@api_view(["DELETE"])
def delete_task(request,task_id):
    try:
        task=Task.objects.get(id=task_id)
        task.delete()
        return Response({"message":"Deleted it "},status=200)
    except:
        return Response({"message":"Didn't found the task"},status=404)
    

@api_view(["PUT"])
def update_task(request,task_id):
    data=request.data.get('title')
    try:
        task=Task.objects.get(id=task_id)
        task.title=data
        task.save()
        return Response({"message":"Updated it"},status=200)
    except:
        return Response({"message":"Didn't found the task"},status=404)