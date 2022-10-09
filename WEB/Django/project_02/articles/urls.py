from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000 들어가면 바로 뜨는 페이지
    path('', views.index),
    path('create/', views.create),
]