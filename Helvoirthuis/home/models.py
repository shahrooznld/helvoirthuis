from django.db import models
from django.utils import timezone


# Create your models here.


class posts(models.Model):
    post_title = models.CharField(max_length=200, null=False)
    post_Article = models.TextField()
    post_images = models.FileField(upload_to='uploads/', null=True)
    post_time = models.DateTimeField(default=timezone.now, null=False)
    post_auther = models.CharField(max_length=20, null=False)


class Contact(models.Model):
    name = models.CharField(max_length=80, null=False)
    contacttime = models.DateTimeField(default=timezone.now, null=False)
    email = models.EmailField(max_length=80, null=False)
    category = models.CharField(max_length=80, null=False)
    subject = models.CharField(max_length=80, null=False)
    body = models.TextField(null=False)

    def __str__(self):
        return self.name


class menutab(models.Model):
    menu_title = models.CharField(max_length=40, null=False)
    menu_adres = models.TextField(null=True)

