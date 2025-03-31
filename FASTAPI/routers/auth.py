#importamos httpexception para manejar errores
from fastapi.responses import JSONResponse
# importamos la libreria para permitir datos opcionales
from modelsPydantic import  modelAuth
from tokenGen import createToken
from fastapi import APIRouter


routerAuth=APIRouter()



#endpoint para token
@routerAuth.post('/auth', tags=['Autenticación'])
def login(autorizado:modelAuth):
    if autorizado.correo == "estrella@example.com" and autorizado.passw == "12345678":
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso":"Usuario no autorizado"}