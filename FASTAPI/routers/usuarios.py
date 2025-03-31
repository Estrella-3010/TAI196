#importamos httpexception para manejar errores
from fastapi import HTTPException,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# importamos la libreria para permitir datos opcionales
from modelsPydantic import modelUsuario
from middelwares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

# declaracion del objeto y la instaciamos de la clase FastAPI
routerUsuario=APIRouter()
#depemdemncies=[Depends(BearerJWT())] #se le pasa la dependencia al endpoint para que valide el token

#endpoint para consultar todos los usuarios
@routerUsuario.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db=Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500,
                            content={"mensaje":"No fue posible consultar",
                                     "error":str(x)})
    finally:
        db.close()

#endpoint consulta por id 
@routerUsuario.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarUno(id:int):
    db=Session()
    try:
        #busca el usuario que solicito en la lista de usuarios el filter funciona como un where 
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500,
                            content={"mensaje":"No fue posible consultar",
                                     "error":str(x)})
    finally:
        db.close()

#endpont para agregar usuarios, la diagonal indica que es un parametro  
@routerUsuario.post('/usuarios/',response_model=modelUsuario, tags=['Operaciones CRUD'])
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

@routerUsuario.put('/usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def ActualizarUsuario(id:int, usuario_actualizado:modelUsuario):
    db=Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"Mensaje":"Usuario no encontrado"})
        for key, value in usuario_actualizado.model_dump().items():
            setattr(consulta, key, value)
        db.commit()
        return JSONResponse(status_code=200,
                            content={"mensaje":"Usuario actualizado",
                                     "usuario":usuario_actualizado.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje":"Error al actualizar el usuario",
                                     "error":str(e)})
    finally: 
        db.close()

@routerUsuario.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def EliminarUsuario(id:int):
    db=Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404,content={"Mensaje":"Usuario no encontrado"})
        usuario_eliminado = jsonable_encoder(consulta)
        db.delete(consulta)
        db.commit()
        return JSONResponse(status_code=200,
                            content={"mensaje":"Usuario eliminado",
                                     "usuario":usuario_eliminado})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje":"Error al eliminar el usuario",
                                     "error":str(e)})
    finally: 
        db.close()
