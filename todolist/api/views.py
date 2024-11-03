from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer
from .models import Task


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
