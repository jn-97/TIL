from django.shortcuts import redirect, render
from .models import Review

# Create your views here.
def index(request):
    
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'movies/index.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):

    title = request.GET.get('title')
    content = request.GET.get('content')

    Review.objects.create(title=title, content=content)

    return redirect('movies:index')

def detail(request, pk_):

    review = Review.objects.get(pk=pk_)
    context = {
        'review': review,
    }

    return render(request, 'movies/detail.html', context)

def edit(request, pk_):

    review = Review.objects.get(pk=pk_)
    context = {
        'review': review,
    }

    return render(request, 'movies/edit.html', context)

def update(request, pk_):

    review = Review.objects.get(pk=pk_)

    title_ = request.GET.get('title')
    content_ = request.GET.get('content')

    review.title = title_
    review.content = content_

    review.save()
    
    return redirect('movies:detail', review.pk)

def delete(request, pk_):

    Review.objects.get(pk=pk_).delete()

    return redirect('movies:index')