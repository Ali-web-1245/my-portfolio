# Create your models here.
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=255, blank=True, default="")
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    subject = models.CharField(max_length=200, default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.name