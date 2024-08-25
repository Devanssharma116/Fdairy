from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
