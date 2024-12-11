from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
class Post(Base):
    __tablename__="posts"
    id=Column(Integer, primary_key=True, nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean, server_default='True', nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class vpn(Base):
    __tablename__="vpns"
    direccionIPRoshka=Column(String,nullable=False)
    direccionIPCliente=Column(String,nullable=False)
    clienteExterno=Column(String,nullable=False)
    marcaEquipoRoshka=Column(String,nullable=False)
    versionEquipoRoshka=Column(String,nullable=False)
    marcaEquipoCliente=Column(String,nullable=False)
    versionEquipoCliente=Column(String,nullable=False)
    claveCompartida=Column(String,nullable=False)
    esquemaDeEncriptacion=Column(String,nullable=False)
    grupoDH=Column(String,nullable=False)
    mainOAggressive=Column(String,nullable=False)
    lifetime=Column(Integer,nullable=False)
    encapsulacion=Column(String,nullable=False)
    algoritmoEncriptacion=Column(String,nullable=False)
    pfs=Column(Boolean, nullable=False)
    lifetime=Column(Integer,nullable=False)
    dominioEncriptacionRoshka=Column(String,nullable=False)
    dominoEncriptacionCliente=Column(String,nullable=False)

    