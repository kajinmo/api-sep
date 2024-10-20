from fastapi import FastAPI

app = FastAPI()

# definir a rota
@app.get("/") # recebe requisições GET
def ola_mundo(): #response
        return {'Olá': 'Mundo'}


