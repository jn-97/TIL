from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    
    # form 태그 및 input 태그를 통해 사용자의 입력을 받아 /pong이라는 페이지에 전달
    path('ping/', views.ping),
    path('pong/', views.pong),
]