from pydantic import BaseModel, Field, EmailStr
#Modelo para validacion de datos 
class modelUsuario(BaseModel):
    name:str = Field(...,min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    age:int = Field(...,gt=0, lt=130, description="Edad debe ser mayor a 0 o menor a 130")
    email: str = Field(..., min_length=5,max_length=50,pattern='^[\w\.-]+@[\w\.-]+\.\w+$', example="nombre@example.com", description="el email debe contener @ y .com")

class modelAuth(BaseModel):
    correo:EmailStr 
    passw: str = Field(...,min_length=8,strip_whitespace=True, description="Contraseña debe contener al menos 8 caracteres")