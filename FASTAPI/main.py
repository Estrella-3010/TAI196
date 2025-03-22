#importamos httpexception para manejar errores
from fastapi import FastAPI, HTTPException,Depends
from fastapi.responses import JSONResponse
# importamos la libreria para permitir datos opcionales
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middelwares import BearerJWT
from DB.conexion import Session,engine, Base
from models.modelsDB import User

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title='Mi primer API 196',
    description='Estrella Cuellar',
    version='1.0.1'
)
# se va a encargar de levantar las tablas en la base de datos
Base.metadata.create_all(bind=engine)



#Creamos una lista para la base de datos 
usuarios=[
    {"id":1, "nombre":"Estrella", "edad":20, "correo":"estrella@ejemplo.com"},
    {"id":2, "nombre":"Lucero", "edad":20, "correo":"lu@ejemplo.com"},
    {"id":3, "nombre":"Lalo", "edad":21, "correo":"lalo@ejemplo.com"},
    {"id":4, "nombre":"Domi", "edad":20, "correo":"domi@ejemplo.com"},
]


# endpoint de arranque 
@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}

#endpoint para token
@app.post('/auth', tags=['Autenticación'])
def login(autorizado:modelAuth):
    if autorizado.correo == "estrella@example.com" and autorizado.passw == "12345678":
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso":"Usuario no autorizado"}




#endpoint para consultar todos los usuarios
@app.get('/usuarios',dependencies=[Depends(BearerJWT())], response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endpont para agregar usuarios, la diagonal indica que es un parametro  
@app.post('/usuarios/',response_model=modelUsuario, tags=['Operaciones CRUD'])
#definimos los parametros que recibira el metodo en este caso sera una lista de diccionarios
def AgregarUsuario(usuario:modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"mensaje":"Usuario creado",
                                     "usuario":usuario.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje":"Error al crear el usuario",
                                     "error":str(e)})

    finally: 
        db.close()


#endpoint para actualizar usuarios
@app.put('/usuarios/{id}', response_model=modelUsuario,tags=['Operaciones CRUD'])
def ActualizarUsuaario(id:int, usuario_actualizado:modelUsuario):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail='Usuario no encontrado')

#endpoint para eliminar usuarios
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {'message':'Usuario eliminado'}
    raise HTTPException(status_code=400, detail='Usuario no registrado')





