#importamos httpexception para manejar errores
from fastapi import FastAPI, HTTPException
# importamos la libreria para permitir datos opcionales
from typing import Optional

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title='Mi primer API 196',
    description='Estrella Cuellar',
    version='1.0.1'
)

#Creamos una lista para la base de datos 
usuarios=[
    {"id":1, "nombre":"Estrella", "edad":20},
    {"id":2, "nombre":"Lu", "edad":20},
    {"id":3, "nombre":"Lalo", "edad":21},
    {"id":4, "nombre":"Domi", "edad":20},
]


# endpoint de arranque 
@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}

#endpoint para consultar todos los usuarios
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {'Usuarios Registrados': usuarios}

#endpont para agregar usuarios, la diagonal indica que es un parametro  
@app.post('/usuarios/', tags=['Operaciones CRUD'])
#definimos los parametros que recibira el metodo en este caso sera una lista de diccionarios
def AgregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            # el raise nos permite lanzar una excepcion
            raise HTTPException(status_code=400, detail='El id ya esta registrado')
    
    usuarios.append(usuario)
    return usuario

#endpoint para actualizar usuarios
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def ActualizarUsuaario(id:int, usuario:dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario)
            return {"Usuario Actualizado":usr}
    raise HTTPException(status_code=400, detail='Usuario no encontrado')

#endpoint para eliminar usuarios
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {'message':'Usuario eliminado'}
    raise HTTPException(status_code=400, detail='Usuario no registrado')



