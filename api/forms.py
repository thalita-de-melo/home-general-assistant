from django import forms
from .models import Movies, Compras

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

class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ['produto', 'pessoa', 'categoria']
        labels = {
            'produto': 'Produto',
            'pessoa': 'Quem Adicionou',
            'categoria': 'Categoria',
        }
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'form-control'}),
            'pessoa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }