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
            return redirect('movies-list')
        return render(request, 'movies_create.html', {'form': form})
    

class ChooseRandomMovie(APIView):
    ### choose a random movie from the list
    def get(self, request):
        movies = Movies.objects.all()
        if movies:
            # show in template movies_random.html
            movie = random.choice(movies)
            template = loader.get_template('movies_random.html')
            return HttpResponse(template.render({'movie': movie}))
        

def index(request):
    # send the template index
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    

