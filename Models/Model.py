# models.py
from sqlalchemy import Column, BigInteger, Numeric, Text, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base, engine

# class Location(Base):
#     __tablename__ = "locations"
#     id = Column(BigInteger, primary_key=True, index=True)
#     latitude = Column(Numeric)
#     longitude = Column(Numeric)
#     name_place = Column(Text)
#     devices = relationship("Device", back_populates="location")

# class Device(Base):
#     __tablename__ = "devices"
#     id = Column(BigInteger, primary_key=True, index=True)
#     device_name = Column(Text)
#     installation_date = Column(Date)
#     location_id = Column(BigInteger, ForeignKey("locations.id"))
#     location = relationship("Location", back_populates="devices")

# class Unit(Base):
#     __tablename__ = "unit"
#     id = Column(BigInteger, primary_key=True, index=True)
#     unit = Column(Text)

# class Sensor(Base):
#     __tablename__ = "sensor"
#     id = Column(BigInteger, primary_key=True, index=True)
#     sensor_name = Column(Text)
#     function = Column(Text)
#     device_id = Column(BigInteger, ForeignKey("devices.id"))
#     unit_id = Column(BigInteger, ForeignKey("unit.id"))
#     device = relationship("Device", back_populates="sensors")
#     unit = relationship("Unit", back_populates="sensors")

# class Record(Base):
#     __tablename__ = "record"
#     id = Column(BigInteger, primary_key=True, index=True)
#     sensor_id = Column(BigInteger, ForeignKey("sensor.id"))
#     value = Column(Numeric)
#     time = Column(TIMESTAMP(timezone=True))

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text)
    email = Column(Text)
    secondname = Column(Text)
    person = Column(Numeric)

# class UserDevice(Base):
#     __tablename__ = "user_device"
#     id = Column(BigInteger, primary_key=True, index=True)
#     user_id = Column(BigInteger, ForeignKey("users.id"))
#     device_id = Column(BigInteger, ForeignKey("devices.id"))


# Crear las tablas en la base de datos
Base.metadata.create_all(engine)