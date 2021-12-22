from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)