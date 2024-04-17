from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=(
        ('Not started','Not started'),
        ('In Progress',' In Progress'),
        ('Completed',' Completed'),
    ))
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)


    def __str__(self):
        return f"{self.user}: {self.title}"