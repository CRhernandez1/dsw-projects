from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=128)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
