#importamos httpexception para manejar errores
from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario 
from routers.auth import routerAuth


# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title='Mi primer API 196',
    description='Estrella Cuellar',
    version='1.0.1'
)
# se va a encargar de levantar las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# que hace este app include_router?
app.include_router(routerUsuario)
app.include_router(routerAuth)


# endpoint de arranque 
@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}







