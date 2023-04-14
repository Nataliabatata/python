import sqlite3
from typing import Optional, Text
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Clientes(BaseModel):
    cpf: str
    nome: str
    email: str
    valor: int


def score():
    c=sqlite3.connect('/Users/Ijovem02/coursepython/database/tatoo.db')
    cr=c.cursor()
    cr.execute("""select cpf , sum(valor) from clientes group by cpf""")
    lista=cr.fetchall()
    c.close()
    return dict(lista)

def ler_clientes():
    c=sqlite3.connect('/Users/Ijovem02/coursepython/database/tatoo.db')
    cr=c.cursor()
    cr.execute("""select * from clientes""")
    lista=cr.fetchall()
    c.close()
    return (lista)



def atualizar_registro(cli: Clientes):
    c = sqlite3.connect('/Users/Ijovem02/coursepython/database/tatoo.db')
    cr = c.cursor()
    cr.execute(""" update clientes SET nome = ? , email = ?  where cpf = ? """  , ( cli.nome, cli.email,  cli.cpf ) )
    c.commit()
    c.close()
    return 0

def listar_clientes():
    c = sqlite3.connect('nt')
    cr = c.cursor()
    cr.execute("""sql""")
    c.close()
    return 0

def listar_um(cpf:str):

    print("sql 1 ...")
    c = sqlite3.connect('/Users/Ijovem02/coursepython/database/tatoo.db')
    print("sql 2 ...")


    cr = c.cursor()

    print("sql 3 ...")

    cr.execute(""" SELECT * FROM clientes where cpf = ?   """   , (cpf,))
    
    print("sql 4 ...")

    lista = cr.fetchall()

    print("sql 5 ...")


    c.close()

    print("sql 6 ...")

    return (lista)



@app.post("/gravar")
def gravar(x:Clientes):
    msg = 'gracias sra Natalia, seu cpf esta invalido: ' +  x.nome   + " " + x.cpf
    return {"msg": msg}

@app.put("/atualizar")
def atualizar(x: Clientes):
    atualizar_registro(x)
    msg = ' gracias sr/ sra, recebi seus dados:' 
    return {"msg": msg}


@app.delete("/excluir")
def excluir(cpf: str):
    return {"Hello": "World"}

@app.get("/listar_clientes")
def listar_clientes():
    return ler_clientes()

@app.get("/listar_score")
def listar_score():
    return score()

@app.get("/listar_unico")
def listar_unico(cpf : str):
    x = listar_um(cpf)
    return x

