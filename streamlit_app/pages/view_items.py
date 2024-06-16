import streamlit as st
import pandas as pd
import requests
import pyperclip

API_URL = 'http://localhost:8000/api/lista-compras/'

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

# Função para marcar um item como comprado via API
def marcar_como_comprado(item_ids):
    try:
        response = requests.post(API_URL + 'marcar_como_comprado/', json={'ids': item_ids})
        if response.status_code == 200:
            st.success("Itens marcados como comprados com sucesso!")
        else:
            st.error(f'Erro ao marcar itens como comprados: {response.status_code}')
    except requests.exceptions.RequestException as e:
        st.error(f'Erro de conexão: {e}')

# Exibir itens da API em um DataFrame pandas
items = get_items_from_api()

if items:
    # Transforma os dados em um DataFrame pandas com as colunas desejadas
    df = pd.DataFrame(items, columns=['id', 'produto', 'pessoa', 'categoria', 'data_criacao'])
    st.dataframe(df)

        # Botão para copiar para a área de transferência
    if st.button("Copiar Nomes e Categorias"):
        clipboard_content = ""
        for index, row in df.iterrows():
            clipboard_content += f"{row['produto']} - Categoria: {row['categoria']}\n"

        pyperclip.copy(clipboard_content)
        st.success("Conteúdo copiado para a área de transferência!")

    # Checkbox para marcar como comprado
    selected_ids = st.multiselect("Selecione os itens para marcar como comprados:", df['id'].tolist(), format_func=lambda x: df[df['id'] == x]['produto'].iloc[0])

    # Botão para marcar como comprado
    if st.button("Marcar como Comprado") and selected_ids:
        marcar_como_comprado(selected_ids)

else:
    st.write('Nenhum item encontrado.')
