from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from Database.Base import meta, engine

Model_User = Table(
    "users", meta,
    Column("Id", Integer, primary_key=True),
    Column("Nombre", String(50)),
    Column("Apellido", String(50)),
    Column("Email", String(50)),
    Column("Password", String(100)),
)

meta.create_all(engine)