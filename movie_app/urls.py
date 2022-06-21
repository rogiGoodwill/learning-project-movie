from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:movie_slug>', views.show_one_movie, name='movie-name'),
]
