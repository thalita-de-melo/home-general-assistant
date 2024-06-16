import streamlit as st
from pages import home, add_item, view_items

import requests

import pandas as pd

# table with most common categories
st.title("Página Inicial")
st.write("Bem-vindo à página inicial do seu aplicativo Streamlit.")
st.write("Aqui você encontra uma lista de categorias mais comuns.")

# Defina a URL da sua API Django
API_URL = 'http://localhost:8000/api/compras/'

# Função para obter os itens existentes
def get_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Erro ao buscar dados da API')
        return []

# Exibir itens existentes
items = get_items()

if items:
    df = pd.DataFrame(items)
else:
    df = pd.DataFrame()

def get_most_common_categories(df):
    return df['categoria'].value_counts().head(10)

# show most common categories
most_common_categories = get_most_common_categories(df)
st.table(most_common_categories)
