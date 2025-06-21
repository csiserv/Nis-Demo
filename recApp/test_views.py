from django.test import TestCase, Client
from django.urls import reverse
from recApp.models import Task

class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertIsNotNone(task.created_at)

class TaskViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('task-list')

    def test_task_list_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'recApp/task_list.html')

    def test_task_list_view_post_creates_task(self):
        response = self.client.post(self.url, data={'title': 'New Task'})
        self.assertEqual(Task.objects.count(), 1)
        self.assertRedirects(response, self.url)

# recApp/test_views.py
# from django.test import TestCase

# class TestSanity(TestCase):
#     def test_addition(self):
#         assert 2 + 2 == 4
