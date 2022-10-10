from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()

    return render(request, 'articles/index.html', {'articles': articles})

def new(request):
    return render(request, 'articles/new.html')

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')

    Article.objects.create(title=title, content=content)

    return redirect('articles:index')