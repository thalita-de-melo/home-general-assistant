from django import forms
from .models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['nome', 'pessoa']
        labels = {
            'nome': 'Nome do Filme',
            'pessoa': 'Quem Escolheu',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'pessoa': forms.TextInput(attrs={'class': 'form-control'}),
        }