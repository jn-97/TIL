from django.shortcuts import render
from .models import Article

guestbook = []

# Create your views here.
def index(request):

    # 2. DB에서 가져오기
    guestbook = Article.objects.all()
    # == SELECT * FROM Article

    return render(request, 'articles/index.html', {'guestbook': guestbook})

def create(request):

    content = request.GET.get('content')
    context = {
        'content': content,
    }

    # 1. DB migration 한 후 DB에 저장
    Article.objects.create(content=content)

    return render(request, 'articles/create.html', context)