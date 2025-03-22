import os 
from sqlalchemy import create_engine 
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#nombre de la base de datos
dbName = 'usuarios.sqlite' 
#ruta de la base de datos
base_dir= os.path.dirname(os.path.realpath(__file__))
#unir el nombre de la base de datos con la ruta
dbUrl=f"sqlite:///{os.path.join(base_dir, dbName)}"

#declaración del motor engine, el que se encargara de crear la base de datos con la ruta especificada
engine=create_engine(dbUrl, echo=True)
Session= sessionmaker(bind=engine)
Base = declarative_base()

