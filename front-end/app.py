import streamlit as st
import requests

#URL da API do fastaPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")

st.title("🍿 gerenciador de filmes")

#menu lateral sidebar
menu = st.sidebar.radio("navegacao", ["catalogo"])

if menu == "Catálogo":
    st.subheader("Todos os Filmes 🎥")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes",[])
        if filmes:
              for filme in filmes:
               st.write(f"**{filme['titulo']}** ({filme['ano']}) - {filme['genero']} - ⭐ {filme['avaliacao']}")
               
    
    
    else:
        st.error("Erro ao carregar os filmes.")

      
      