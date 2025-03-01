import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos,key='secret123', algorithm='HS256')
    return token

def validateToken(token:str):
    try:
        data:dict = jwt.decode(token,key='secret123', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=400, detail='Token expirado')
    except InvalidTokenError:
        raise HTTPException(status_code=400, detail='Token no autorizado')
