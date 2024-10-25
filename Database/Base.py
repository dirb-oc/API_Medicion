from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+asyncpg://postgres:1005185673@localhost:5432/Medidor")

meta = MetaData()

con = engine.connect()