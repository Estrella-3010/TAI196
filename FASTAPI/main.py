from fastapi import FastAPI 
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
    {'id':1, 'nombre':'Estrella', 'edad':20},
    {'id':2, 'nombre':'Lu', 'edad':20},
    {'id':3, 'nombre':'Lalo', 'edad':21},
    {'id':4, 'nombre':'Domi', 'edad':20},
]


# endpoint de arranque 
@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}

@app.get('/promedio', tags=['Mi claificaión'])
def promedio():
    return {'Promedio': 9.9}

#endpoint obligatorio
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultarusuario(id:int):
    #conectamosBD
    #hacemos consulta retornamos resultset 
    return{'Se encontro el usuario': id}

#endpoint opcional
@app.get('/usuario2/', tags=['Parametro Opcional'])
def consultarUsuarioOpcional(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario['id'] == id: 
                return {'Usuario encontrado': usuario}
        return {'Mensaje':f'No se encontrado el id: {id}'}
    else:
        return{'mensaje': 'No hay usuarios registrados'}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
