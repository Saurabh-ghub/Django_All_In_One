from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()