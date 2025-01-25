from fastapi import FastAPI 

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI()

# endpoint de arranque 
@app.get('/')
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola FASTAPI':'EstrellaCuellar'}
