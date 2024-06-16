import streamlit as st
import pandas as pd
import requests
import pyperclip

API_URL = 'http://localhost:8000/api/compras/'

st.title("Itens na Lista de Compras")

# Função para obter os itens via API
def get_items_from_api():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f'Erro ao buscar dados da API: {response.status_code}')
            return []
    except requests.exceptions.RequestException as e:
        st.error(f'Erro de conexão: {e}')
        return []

# Exibir itens da API em um DataFrame pandas
items = get_items_from_api()

if items:
    df = pd.DataFrame(items)
    st.dataframe(df)

    # Botão para copiar para a área de transferência
    if st.button("Copiar Nomes e Categorias"):
        clipboard_content = ""
        for index, row in df.iterrows():
            clipboard_content += f"{row['produto']} - Categoria: {row['categoria']}\n"

        pyperclip.copy(clipboard_content)
        st.success("Conteúdo copiado para a área de transferência!")

else:
    st.write('Nenhum item encontrado.')
