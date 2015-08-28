from django.test import TestCase
from task.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title="Task1", description="descriptionTask1")
        Task.objects.create(completed=True, title="Task2", description="descriptionTask2")

    def test_task_to_string(self):
        task1 = Task.objects.get(title="Task1")
        task2 = Task.objects.get(title="Task2")
        self.assertEqual(task1.to_string(), "Titulo = Task1\nCompleto = False")
        self.assertEqual(task2.to_string(), "Titulo = Task2\nCompleto = True")

    def test_task_get_name(self):
        task1 = Task.objects.get(title="Task1")
        self.assertEqual(task1.get_title(), "Task1")
