import streamlit as st
import pandas as pd
import requests

# Defina a URL da sua API Django
api_url = 'http://localhost:8000/api/data/'

# Função para obter dados da API
def get_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Falha ao buscar dados da API')
        return []

# Carregar dados
data = get_data()

# Converter dados em DataFrame
df = pd.DataFrame(data)

# Exibir dados no Streamlit
st.title('Dados do Modelo Movies')
st.dataframe(df)
