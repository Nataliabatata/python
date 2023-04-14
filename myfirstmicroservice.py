from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.post("/salvar")
def salvar():
    return {"Hello": "World"}

@app.get("/ler")
def ler():
    return {"Hello": "World"}

@app.delete("/excluir")
def excluir():
    return {"Hello": "World"}

@app.put("/alterar")
def alterar():
    return {"Hello": "World"}