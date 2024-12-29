from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Vpn(Base):
    __tablename__="vpns"
    id=Column(Integer, primary_key=True, nullable=False)
    nombreClienteExterno=Column(String,nullable=False)
    rol=Column(String,nullable=False)
    direccionIPRoshka=Column(String,nullable=False)
    direccionIPCliente=Column(String,nullable=False)
    marcaEquipoRoshka=Column(String,nullable=False)
    versionEquipoRoshka=Column(String,nullable=False)
    marcaEquipoCliente=Column(String,nullable=False)
    versionEquipoCliente=Column(String,nullable=False)
    claveCompartida=Column(String,nullable=False)
    esquemaDeEncriptacion=Column(String,nullable=False)
    grupoDH=Column(String,nullable=False)
    algoritmoEncriptacion_fase1=Column(String,nullable=False)
    hash_fase1=Column(String,nullable=False)
    mainOAggressive=Column(String,server_default='Main',nullable=False)
    lifetime_fase1=Column(Integer,nullable=False)
    encapsulacion=Column(String,server_default='ESP',nullable=False)
    algoritmoEncriptacion_fase2=Column(String,nullable=False)
    hash_fase2=Column(String,nullable=False)
    pfs=Column(String, nullable=False)
    lifetime_fase2=Column(Integer,nullable=False)
    dominioEncriptacionRoshka=Column(String,nullable=False)
    dominoEncriptacionCliente=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


def vpn_to_json(self):
        return {
            'id':self.id,
            'nombreClienteExterno':self.nombreClienteExterno,
            'rol':self.rol,
            'direccionIPRoshka':self.direccionIPRoshka,
            'direccionIPCliente':self.direccionIPCliente,
            'marcaEquipoRoshka':self.marcaEquipoRoshka,
            'versionEquipoRoshka':self.versionEquipoRoshka,
            'marcaEquipoCliente':self.marcaEquipoCliente,
            'versionEquipoCliente':self.versionEquipoCliente,
            'claveCompartida':self.claveCompartida,
            'esquemaDeEncriptacion':self.esquemaDeEncriptacion,
            'grupoDH':self.grupoDH,
            'algoritmoEncriptacion_fase1':self.algoritmoEncriptacion_fase1,
            'hash_fase1':self.hash_fase1,
            'mainOAggressive':self.mainOAggressive,
            'lifetime_fase1':self.lifetime_fase1,
            'encapsulacion':self.encapsulacion,
            'algoritmoEncriptacion_fase2':self.algoritmoEncriptacion_fase2,
            'hash_fase2':self.hash_fase2,
            'pfs':self.pfs,
            'lifetime_fase2':self.lifetime_fase2,
            'dominioEncriptacionRoshka':self.dominioEncriptacionRoshka,
            'dominoEncriptacionCliente':self.dominoEncriptacionCliente,
            'created_at':self.created_at
        }