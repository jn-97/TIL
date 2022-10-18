from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField()
    running_time = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True)
