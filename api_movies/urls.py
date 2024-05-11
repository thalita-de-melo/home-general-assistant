from django.contrib import admin
from django.urls import path

from api.views import MoviesList, MoviesCreateView, index, ChooseRandomMovie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MoviesList.as_view(), name='movies-list'),
    path('movies/create/', MoviesCreateView.as_view(), name='movies-create'),
    path('home/', index, name='index'),
    path('movies/random/', ChooseRandomMovie.as_view(), name='random-movie'),
]
