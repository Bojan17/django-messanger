from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created_at"]
