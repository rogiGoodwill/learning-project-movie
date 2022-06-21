from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Max, Min, Sum, Count, Avg, Value


# Create your views here.

def show_all_movie(request):
    #movies = Movie.objects.order_by('name')
    movies = Movie.objects.annotate(
        sum_rating_year=F('rating') + F('year')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, movie_slug: str):
    movie = get_object_or_404(Movie, slug=movie_slug)
    return render(request, 'movie_app/one_movies.html', {
        'movie': movie,
    })
