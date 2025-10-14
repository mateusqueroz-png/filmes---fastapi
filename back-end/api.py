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


@app.get("/filmes")
def catalogo():
    filmes = funcao.listar_movies()
    lista = []
    for filme in filmes:
        lista.append( { 
            "id":filme[0],
            "titulo": filme[1],
            "genero": filme[2],
            "ano": filme[3],
            "avaliacao": filme[4] 
            } )
    return{"filmes":lista}

@app.post("/filmes")
def adicionar_filme(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.criar_filme(titulo,genero,ano,avaliacao)
    return{"mensagem": "F ilmes adicionar com sucesso"}


