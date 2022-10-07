from email.policy import default
from django.db import models

# Create your models here.

class Movie(models.Model):
    # 영화 제목
    title = models.TextField()
    # 줄거리
    summary = models.TextField()
    # 영화 상영 시간
    running_time = models.CharField(max_length=10, default=0)