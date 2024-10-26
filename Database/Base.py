from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Oo1005185673@localhost:3306/Prueba")

meta = MetaData()

conn = engine.connect()