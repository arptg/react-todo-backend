from django.db import models
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TodoLabel(Timestamp):
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(
        max_length=255, null=True, default=None, blank=True)
    done = models.BooleanField(default=False, blank=True)
    label = models.ForeignKey(
        TodoLabel, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.id})"
