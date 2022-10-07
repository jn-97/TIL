from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')

def create(request):

    # 1. parameter로 날아온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. DB에 저장
    Post.objects.create(title=title, content=content)

    context = {
        'title' : title,
        'content' : content,
    }

    return render(request, 'posts/create.html', context)