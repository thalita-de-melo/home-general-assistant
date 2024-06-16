import random
import json

from django.shortcuts import render

from rest_framework import generics
from .models import Movies, Compras
from .serializers import MoviesSerializer, ComprasSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect
from .forms import MoviesForm

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
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

@method_decorator(csrf_exempt, name='dispatch')
class ComprasAddItem(APIView):
    def get(self, request):
        items = list(Compras.objects.values())
        return JsonResponse(items, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            produto = data.get('produto')
            pessoa = data.get('pessoa')
            categoria = data.get('categoria')
            comprado = False
            data_comprado = None

            if not all([produto, pessoa, categoria]):
                return JsonResponse({'error': 'Missing fields'}, status=400)

            new_item = Compras.objects.create(
                produto=produto,
                pessoa=pessoa,
                categoria=categoria,
                comprado=comprado,
                data_comprado=data_comprado
            )

            return JsonResponse({
                'id': new_item.id,
                'produto': new_item.produto,
                'pessoa': new_item.pessoa,
                'categoria': new_item.categoria,
                'data_criacao': new_item.data_criacao,
                'comprado': new_item.comprado,
                'data_comprado': new_item.data_comprado
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class GetListaCompras(APIView):
    def get(self, request):
        items = Compras.objects.exclude(comprado=True)
        serializer = ComprasSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        try:
            item = Compras.objects.get(pk=request.data['id'])
            item.comprado = True
            item.data_comprado = datetime.datetime.now()
            item.save()
            return Response({'message': 'Item comprado com sucesso.'}, status=status.HTTP_200_OK)
        except Compras.DoesNotExist:
            return Response({'error': 'Item não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

from django.shortcuts import render, redirect
from .forms import ComprasForm

def compras_create(request):
    categorias = [
    "Alimentos",
    "Bebidas",
    "Limpeza",
    "Higiene Pessoal",
    "Frutas e Verduras",
    "Carnes e Frios",
    "Laticínios",
    "Padaria",
    "Confeitaria",
    "Pet Shop"
    ]

    pessoas = [
        'Thalita',
        'Vivian'
    ]
    if request.method == 'POST':
        form = ComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página de lista de compras após salvar
    else:
        form = ComprasForm()

    items = Compras.objects.exclude(comprado=True).order_by('-data_criacao')
    
    return render(request, 'compras_create.html', {'form': form, 'categorias': categorias, 'pessoas': pessoas, 'items': items})

def get_data(request):
    data = list(Movies.objects.values())
    return JsonResponse(data, safe=False)

from django.shortcuts import render

def show_chart(request):
    return render(request, 'chart.html')

def index(request):
    # send the template index
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    

