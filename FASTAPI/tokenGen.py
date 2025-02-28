import jwt

def createToken(datos:dict):
    token:str = jwt.encode(payload=datos,key='secret123', algorithm='HS256')