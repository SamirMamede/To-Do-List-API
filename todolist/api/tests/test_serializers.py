from django.test import TestCase
from django.utils import timezone
from api.serializer import TaskSerializer
from api.models import Task

class TaskSerializerTests(TestCase):
    def test_contains_expected_fields(self):
        task = Task.objects.create(title="Teste")
        serializer = TaskSerializer(task)
        
        expected_fields = {
            'id',
            'title',
            'description',
            'completed',
            'created_at',
            'completed_at'
        }
        
        self.assertEqual(set(serializer.data.keys()), expected_fields)

    def test_title_field_required(self):
        data = {
            'description': 'Teste',
            'completed': False
        }
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)

    def test_valid_data_serialization(self):
        data = {
            'title': 'Teste',
            'description': 'Descrição teste',
            'completed': True
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())