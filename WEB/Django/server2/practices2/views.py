from django.shortcuts import render
from .models import Practices2
# Create your views here.

guestbook = []

def index(request):
    guestbook = Practices2.objects.all()
    # SELECT * FROM practices2;
    return render(request, 'practices2/index.html', {'guestbook': guestbook})

def create(request):
    content = request.GET.get('content')

    # DB에 저장
    Practices2.objects.create(content=content)

    return render(request, 'practices2/create.html', {'content': content})

    # DB 생성
    # 1. python manage.py makemigrations
    # 2. python manage.py migrate