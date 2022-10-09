from django.urls import path
from . import views

# app_name을 작성하면 name 변수가 중복되어도 articles안에서만 적용되기 때문에 중복 걱정 X
app_name = 'articles'
urlpatterns = [
    # localhost:8000 들어가면 바로 뜨는 페이지
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]