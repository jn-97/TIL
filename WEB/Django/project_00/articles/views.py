from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):

    # all('-pk') = 가져온 정보들을 내림차순으로 정렬해서 띄워줌
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)

    # 입력한 페이지로 바로 돌아가기
    return redirect('articles:index')