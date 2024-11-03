from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from api.models import Task

class TaskModelTests(TestCase):
    def test_create_task_defaults(self):
        task = Task.objects.create(title="Teste")
        self.assertEqual(task.title, "Teste")
        self.assertFalse(task.completed)
        self.assertIsNone(task.completed_at)
        self.assertIsInstance(task.created_at, datetime)
        self.assertTrue(task.description == "" or task.description is None)

    def test_str_representation(self):
        task = Task.objects.create(title="Minha Tarefa")
        self.assertEqual(str(task), "Minha Tarefa")

    def test_complete_task(self):
        task = Task.objects.create(title="Teste", completed=True)
        self.assertIsNotNone(task.completed_at)
        self.assertTrue(task.completed)

    def test_uncomplete_task(self):
        task = Task.objects.create(title="Teste", completed=True)
        self.assertIsNotNone(task.completed_at)
        
        task.completed = False
        task.save()
        self.assertIsNone(task.completed_at)

    def test_update_task_without_changing_completion(self):
        task = Task.objects.create(title="Teste", completed=True)
        original_completed_at = task.completed_at
        
        task.title = "Novo título"
        task.save()
        
        self.assertEqual(task.completed_at, original_completed_at)