import streamlit as st
import requests

#URL da API do fastaPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")

st.title("🍿 gerenciador de filmes")

#menu lateral sidebar
menu = st.sidebar.radio("Navegacao", ["Catalogo","Adicionar Filme"])

if menu == "Catalogo":
    st.subheader("Todos os Filmes 🎥")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes",[])
        if filmes:
              for filme in filmes:
               st.write(f"**{filme['titulo']}** ({filme['ano']}) - {filme['genero']} - ⭐ {filme['avaliacao']}")
        else:
            st.info("Nenhum filme cadastrado")       
    
    else:
        st.error("Erro ao carregar os filmes.")

      
elif menu == "Adicionar Filme":
    st.subheader("➕ Adicionar Filme")
    titulo = st.text_input("Titulo do filme")
    genero = st.text_input("Genero")
    ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=2100)
    avaliacao = st.number_input("Avaliação de (0 a 10)", min_value=0, max_value=10, step=1)

    if st.button("Salvar filme"):
        params = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes", params=params)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesoo!")
        else:
            st.error("Erro ao adicionar o filme")