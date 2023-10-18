from django.db import models

# Create your models here.

class Post(models.Model):
   
    rows = models.CharField(max_length=200)
    columns = models.TextField()
    