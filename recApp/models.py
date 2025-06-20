from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # a short text field
    completed = models.BooleanField(default=False)  # true/false field
    created_at = models.DateTimeField(auto_now_add=True)  # auto-set on creation

    def __str__(self):
        return self.title  # shown in admin panel
