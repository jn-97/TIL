from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("detail/", views.detail, name="detail"),
]
