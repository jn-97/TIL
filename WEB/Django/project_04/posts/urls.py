from django.urls import path
from . import views


"""
메인(R) : 게시글의 목록(/posts/) / 게시글 상세
작성(C) : 글을 작성하는 페이지(/posts/new/) / 작성 완료하는 페이지(/posts/create/)
수정(U) : 글을 수정하는 페이지 / 수정 완료하는 페이지
삭제(D) : 글 삭제 완료
"""

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'), # 게시글의 목록
    path('new/', views.new, name='new'), # 글을 작성하는 페이지
    path('create/', views.create, name='create'), # 글 작성 완료하는 페이지
    path('delete/<int:pk>', views.delete, name='delete'), # 글 삭제하는 페이지
]