from pydantic import BaseModel, Field

class modelenvio(BaseModel):
    codigoPostal:str=Field(...,min_length=5,description="Codigo postal debe contener 5 digitos")
    destino:str=Field(...,min_length=6,max_length=50,description="Destino debe contener solo letras y espacios")
    peso:int=Field(...,gt=0,lt=500,description="Peso debe ser mayor a 0")