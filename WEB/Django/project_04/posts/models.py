from django.db import models

# Create your models here.
class Post(models.Model):
    # You are trying to add a non-nullable field '필드명' to post without a default; we can't do that (the database needs something to populate existing rows).
    # 이런 오류가 뜰 때에는 옵션에 null=True 또는 default=''를 추가해준다.
    title = models.CharField(null=True, default='', max_length=50)
    content = models.TextField(null=True, default='')