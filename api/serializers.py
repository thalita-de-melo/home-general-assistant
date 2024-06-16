from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movies, Compras

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'nome', 'pessoa', 'data_criacao', 'assistido', 'data_assistido'	]

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['id', 'produto', 'pessoa', 'categoria', 'data_criacao', 'comprado', 'data_comprado']