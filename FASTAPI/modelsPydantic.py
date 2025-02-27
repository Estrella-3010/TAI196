from pydantic import BaseModel, Field
#Modelo para validacion de datos 
class modelUsuario(BaseModel):
    id:int = Field(...,gt=0, description="ID único y numero positivo")
    nombre:str = Field(...,min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    edad:int = Field(...,gt=0, lt=130, description="Edad debe ser mayor a 0 o menor a 130")
    correo: str = Field(..., min_length=5,max_length=50,pattern='^[\w\.-]+@[\w\.-]+\.\w+$', example="nombre@example.com", description="el email debe contener @ y .com")
