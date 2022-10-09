from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):

    # 모든 글 목록 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. templates에 보내준다.
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):

    # 1. new.html에서 날아온 데이터를 가져와서
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 2. DB에 저장
    Post.objects.create(title=title, content=content)
    # title(DB에 저장된 이름)=title(1.에서 날아온 데이터를 저장한 변수명)

    context = {
        'title': title,
        'content': content,
    }

    return redirect('posts:index')

def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')