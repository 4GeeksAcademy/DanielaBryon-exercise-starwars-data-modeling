import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    firstname = Column(String(60), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    address = Column(String(250), nullable=False)
    phone = Column(String(40), nullable=False)
    password = Column(String(80), nullable=False)
    #relaciones
    #ATENCION: quise utilizar el backref de la clase, pero no se si lo he implementado bien
    likes = relationship('Favourites', backref='user')

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), unique=True, nullable=False)
    gravedad = Column(String(60))
    diametro = Column(String(60))
    poblacion = Column(String(80))
    descripcion = Column(String(250))
    #relaciones

    likes = relationship('Favourites', back_populates='planet')

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True, nullable=False)
    peso = Column(String(70))
    color_ojos = Column(String(60))
    sexo = Column(Enum('Men','Women','NaN'), nullable=False)
    color_pelo = Column(String(50))
    #relaciones

    likes = relationship('Favourites', back_populates='character')

class Favourites(Base):
    __tablename__ = 'favourites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_planetas = Column(Integer, ForeignKey('planets.id'),  nullable=True)
    id_personajes = Column(Integer, ForeignKey('characters.id'),  nullable=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    #relaciones

    planet = relationship('Planets', back_populates="likes")
    character = relationship('Characters', back_populates='likes')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
