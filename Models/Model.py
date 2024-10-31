# models.py
from sqlalchemy import Column, BigInteger, Numeric, Text, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from Database.Base import Base, engine

class Location(Base):
    __tablename__ = "locations"
    id = Column(BigInteger, primary_key=True, index=True)
    latitude = Column(Text)
    longitude = Column(Text)
    name_place = Column(Text)
    devices = relationship("Device", back_populates="location")

class Device(Base):
    __tablename__ = "devices"
    id = Column(BigInteger, primary_key=True, index=True)
    device_name = Column(Text)
    installation_date = Column(Date)
    location_id = Column(BigInteger, ForeignKey("locations.id"))
    location = relationship("Location", back_populates="devices")
    sensors = relationship("Sensor", back_populates="device")
    users = relationship("UserDevice", back_populates="device")

class Unit(Base):
    __tablename__ = "unit"
    id = Column(BigInteger, primary_key=True, index=True)
    unit = Column(Text)
    sensors = relationship("Sensor", back_populates="unit")

class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(BigInteger, primary_key=True, index=True)
    sensor_name = Column(Text)
    function = Column(Text)
    device_id = Column(BigInteger, ForeignKey("devices.id"))
    unit_id = Column(BigInteger, ForeignKey("unit.id"))
    device = relationship("Device", back_populates="sensors")
    unit = relationship("Unit", back_populates="sensors")
    records = relationship("Record", back_populates="sensor")

class Record(Base):
    __tablename__ = "record"
    id = Column(BigInteger, primary_key=True, index=True)
    sensor_id = Column(BigInteger, ForeignKey("sensor.id"))
    value = Column(Numeric)
    time = Column(TIMESTAMP(timezone=True))
    sensor = relationship("Sensor", back_populates="records")

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(Text)
    email = Column(Text)
    secondname = Column(Text)
    person = Column(Numeric)
    devices = relationship("UserDevice", back_populates="user")

class UserDevice(Base):
    __tablename__ = "user_device" 
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    device_id = Column(BigInteger, ForeignKey("devices.id"), nullable=False)
    user = relationship("User", back_populates="devices")
    device = relationship("Device", back_populates="users")

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)