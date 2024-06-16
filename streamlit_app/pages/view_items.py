import streamlit as st
import pandas as pd
import requests

API_URL = 'http://localhost:8000/api/compras/'


st.title("Itens na Lista de Compras")

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
    st.dataframe(df)
else:
    st.write('Nenhum item encontrado.')
