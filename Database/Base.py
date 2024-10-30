from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "postgresql://postgres:1005185673@localhost:5432/Medidor"
DATABASE_URL = "postgresql://orlando:2TNKEuccZQY02IV0KQxENy7sykDingap@dpg-csgsgibtq21c73dv2fm0-a.oregon-postgres.render.com/mediciondb"


# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase base
Base = declarative_base()
db: Session = SessionLocal()