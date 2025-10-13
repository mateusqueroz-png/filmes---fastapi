from fastapi import FastAPI
import funcao

#Roda fastapi = python -m unicorn api:app --reload

#Tstar as rotas no fastapi
# /docs > documentos Swagger
# /redoc > Documentação redoc

app = FastAPI(title ="Gerenciador de Filmes")

#GET > pegar/Listar
#POST > Eviar/CAdastrar
#PUT > Atualizar
#DELETE > deletar

#API sempre retorna dados em JSON (Chave: valor)
@app.get("/")
def home():
    return {"Mensagem":"Bem - vindo ao gerenciador de filmes"}
