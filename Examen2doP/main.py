from fastapi import FastAPI, HTTPException 
from typing import List 
from modelo import modelenvio 


app = FastAPI(
    title='Examen S196',
    description='Estrella Cuellar',
    version='1.0.1'
)

envios = [
    {"codigoPostal":"76720", "destino":"pedroEscobedo", "peso":20},
    {"codigoPostal":"76000", "destino":"queretaro", "peso":15},
    {"codigoPostal":"76230", "destino":"elmarques", "peso":10},
]

#crea un endpoint para agregar envios
@app.post('/envios/', response_model=modelenvio, tags=['Envios'])
def agregar(envio:modelenvio):
    for env in envios:
        if env["codigoPostal"] == envio.codigoPostal:
            raise HTTPException(status_code=400, detail="Envio ya existente")
    envios.append(envio.model_dump())
    return envio



@app.get('/envios/{codigoPostal}',response_model=modelenvio, tags=['Envios'])
def consultar(codigoPostal:str):
    for env in envios:
        if env["codigoPostal"] == codigoPostal:
            return env
    raise HTTPException(status_code=400, detail="Envio no encontrado")

@app.put('/envios/{codigoPostal}', response_model=modelenvio, tags=['Envios'])
def actualizar(codigoPostal:str, envioactualizado:modelenvio):
    for index,env in enumerate(envios):
        if env["codigoPostal"] == codigoPostal:
            envios[index] = envioactualizado.model_dump()
            return envioactualizado
    raise HTTPException(status_code=400, detail="Envio no encontrado")

# uvicorn main:app 
