from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'nome', 'pessoa', 'assistido']
