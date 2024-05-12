import random

from django.shortcuts import render

from rest_framework import generics
from .models import Movies
from .serializers import MoviesSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect
from .forms import MoviesForm

from django.http import HttpResponse
from django.template import loader
import datetime


class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesCreateView(APIView):
    def get(self, request):
        form = MoviesForm()
        return render(request, 'movies_create.html', {'form': form})

    def post(self, request):
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'movies_create.html', {'form': form})
    

class ChooseRandomMovie(APIView):
    # choose a random movie from the list
    def get(self, request):
        movies = Movies.objects.exclude(assistido=True)
        if movies:
            movie = random.choice(movies)
            template = loader.get_template('movies_random.html')
            return HttpResponse(template.render({'movie': movie}))
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'No movies available'})
        
class ChangeMovieStatus(APIView):
    def post(self, request, movie_id):
        try:
            movie = Movies.objects.get(pk=movie_id)
            movie.assistido = True
            movie.data_assistido = datetime.datetime.now()
            movie.save()
            return redirect('index')
        except Movies.DoesNotExist:
            return Response({'error': 'Filme não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteMovie(APIView):
    def post(self, request):
        try:
            movie = Movies.objects.get(pk=request.data['id'])
            movie.delete()
            return Response({'message': 'Filme deletado com sucesso.'}, status=status.HTTP_200_OK)
        except Movies.DoesNotExist:
            return Response({'error': 'Filme não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

def index(request):
    # send the template index
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    

