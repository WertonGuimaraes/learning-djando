from django.test import TestCase
from task.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title="lion", description="roar")
        Task.objects.create(completed=True, title="cat", description="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Task.objects.get(title="lion")
        cat = Task.objects.get(title="cat")
        self.assertEqual(lion.to_string(), "Titulo = lion\nCompleto = False")
        self.assertEqual(cat.to_string(), "Titulo = cat\nCompleto = True")
