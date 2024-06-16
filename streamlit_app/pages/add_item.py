import streamlit as st
import requests

API_URL = 'http://localhost:8000/api/compras/'


st.title("Adicionar Novo Item")

# Lista de categorias de produtos de mercado
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

# Formulário para adicionar um novo item
with st.form('add_item_form'):
    produto = st.text_input('Produto')
    pessoa = st.text_input('Pessoa')
    categoria = st.selectbox('Categoria', categorias)

    submitted = st.form_submit_button('Adicionar')
    if submitted:
        item_data = {
            'produto': produto,
            'pessoa': pessoa,
            'categoria': categoria,
            'comprado': False,
            'data_comprado': None
        }
        response = requests.post(API_URL, json=item_data)
        if response.status_code == 201:
            st.success('Item adicionado com sucesso!')
        else:
            st.error('Erro ao adicionar item: {}'.format(response.json().get('error')))
