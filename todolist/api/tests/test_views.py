from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Task

class TaskViewsTests(APITestCase):
    def setUp(self):
        
        Task.objects.create(title="Tarefa 1", description="Descrição da tarefa 1", completed=False)
        Task.objects.create(title="Tarefa 2", description="Descrição da tarefa 2", completed=True)

    def test_get_tasks(self):
        
        url = reverse('get_tasks')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 2)