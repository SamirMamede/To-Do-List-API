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

    def test_create_task_minimal_data(self):
        url = reverse('create_task')
        payload = {
            'title': 'Nova Tarefa'
        }

        response = self.client.post(url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(response.data['title'], 'Nova Tarefa')
        self.assertFalse(response.data['completed'])

    def test_create_task_all_fields(self):
        url = reverse('create_task')
        payload = {
            'title': 'Tarefa Completa',
            'description': 'Descrição detalhada da tarefa',
            'completed': True
        }

        response = self.client.post(url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Tarefa Completa')
        self.assertEqual(response.data['description'], 'Descrição detalhada da tarefa')
        self.assertTrue(response.data['completed'])

    def test_create_task_invalid_data(self):
        url = reverse('create_task')
        payload = {
            'description': 'Descrição sem título'
        }

        response = self.client.post(url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_detail(self):
        task = Task.objects.first()
        url = reverse('task_detail', args=[task.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tarefa 1')
        self.assertEqual(response.data['description'], 'Descrição da tarefa 1')
        self.assertFalse(response.data['completed'])

    def test_get_task_detail_not_found(self):
        url = reverse('task_detail', args=[999])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_task(self):
        task = Task.objects.first()
        url = reverse('task_detail', args=[task.id])
        payload = {
            'title': 'Tarefa Atualizada',
            'description': 'Nova descrição',
            'completed': True
        }
        
        response = self.client.put(url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tarefa Atualizada')
        self.assertEqual(response.data['description'], 'Nova descrição')
        self.assertTrue(response.data['completed'])

    def test_update_task_invalid_data(self):
        task = Task.objects.first()
        url = reverse('task_detail', args=[task.id])
        payload = {
            'title': ''
        }
        
        response = self.client.put(url, payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_task(self):
        task = Task.objects.first()
        url = reverse('task_detail', args=[task.id])
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)

    def test_delete_task_not_found(self):
        url = reverse('task_detail', args=[999])
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)