#importamos httpexception para manejar errores
from fastapi import FastAPI, HTTPException
# importamos la libreria para permitir datos opcionales
from typing import Optional

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title='Administrar Tareas',
    description='Estrella Cuellar',
    version='1.0.1'
)

#Creamos una lista para la base de datos 
tareas=[
    {"id":1, "titulo":"Tarea 1", "descripción":"Realizar los ejercicios","fecha_vencimiento":"19-02-2025", "estado":"pendiente"},
    {"id":2, "titulo":"Tarea 2", "descripción":"Realizar un ensayo","fecha_vencimiento":"18-02-2025", "estado":"pendiente"},
    {"id":3, "titulo":"Tarea 3", "descripción":"Realizar un programa","fecha_vencimiento":"17-02-2025", "estado":"pendiente"},
    {"id":4, "titulo":"Tarea 4", "descripción":"Realizar una investigación","fecha_vencimiento":"20-02-2025", "estado":"pendiente"},
]

@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola Api Tareas':'EstrellaCuellar'}

#endpoint para consultar todas las tareas
@app.get('/tareas', tags=['Operaciones CRUD'])
def ConsultarTareas():
    return {'Tareas Registradas': tareas}

#endpont para consultar una tarea por id
@app.get('/tareas/{id}', tags=['Operaciones CRUD'])
def ConsultarTarea(id:int):
    for tar in tareas:
        if tar["id"] == id:
            return tar
    raise HTTPException(status_code=400, detail='Tarea no encontrada')

#endpont para agregar tareas, la diagonal indica que es un parametro
@app.post('/tareas/', tags=['Operaciones CRUD'])
#definimos los parametros que recibira el metodo en este caso sera una lista de diccionarios
def AgregarTarea(tarea:dict):
    for tar in tareas:
        if tar["id"] == tarea.get("id"):
            # el raise nos permite lanzar una excepcion
            raise HTTPException(status_code=400, detail='El id ya esta registrado')
    
    tareas.append(tarea)
    return tarea

