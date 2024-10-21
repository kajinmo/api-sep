from fastapi import FastAPI
from typing import List, Dict


app = FastAPI()


produtos: List[Dict[str, any]] = [
    {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um telefone que é inteligente",
            "preco": 1500.0,
            "disponivel": True, 
    },
    {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um computador que é móvel",
            "preco": 3500.0,
            "disponivel": False, 
    },
    {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um dispositivo móvel",
            "preco": 2500.0,
            "disponivel": True, 
    },
]


# definir a rota
@app.get("/") # recebe requisições GET
def ola_mundo(): #response
        return {'Olá': 'Muundo'}

# definir a rota que puxa produto
@app.get("/produtos")
def listar_produtos():
        return produtos

