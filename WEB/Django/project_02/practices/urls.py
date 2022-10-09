from django.urls import path
from . import views

app_name = 'practices'
urlpatterns = [
    # name 변수는 모든 templates에 공통 적용되기 때문에 app_name 설정하기
    path('index/', views.index, name="index"),
    
    # form 태그 및 input 태그를 통해 사용자의 입력을 받아 /pong이라는 페이지에 전달
    path('ping/', views.ping, name="ping"),
    path('pong/', views.pong, name="pong"),
]