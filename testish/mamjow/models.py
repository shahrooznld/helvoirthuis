from django.db import models


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    age = models.IntegerField()


class posts(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    bodytext= models.TextField()
    timestamp = models.DateTimeField()
