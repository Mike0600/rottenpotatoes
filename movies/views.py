
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Director

# Create your views here.


def index(request):
    if request.GET:
        movie_name = request.GET['search']
        movies = Movie.objects.filter(name__contains = f'{movie_name}')
        return render(request, 'movies/index.html', {
            'movies': movies,
        })
    else:
        movies = Movie.objects.all().order_by('-year')
        return render(request, 'movies/index.html', {
            'movies' : movies,
        })