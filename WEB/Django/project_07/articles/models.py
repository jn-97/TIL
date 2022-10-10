from django.db import models

# Create your models here.
"""
게시판 기능
- 제목
- 내용
- 글 작성시간/수정시간
"""

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)