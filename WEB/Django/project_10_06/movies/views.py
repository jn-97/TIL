from django.shortcuts import render
from .models import Movie

# Create your views here.
def movies(request):
    title = request.GET.get('title')
    summary = request.GET.get('summary')
    running_time = request.GET.get('running_time')

    Movie.objects.create(title=title, summary=summary, running_time=running_time)

    context = {
        'title' : title,
        'summary': summary,
        'running_time': running_time,
    }

    # IntegrityError: NOT NULL constraint failed: movies_movie.title
    return render(request, 'movies/movies.html', context)

def create(request):

    return render(request, 'movies/create.html')