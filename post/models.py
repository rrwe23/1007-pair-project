from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.TextField()
    summary = models.TextField()

