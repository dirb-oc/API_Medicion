from sqlalchemy import Column, Integer, String
from Database.Base import Base, engine

# Definición del modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)