from pydantic import BaseModel
class PostBase(BaseModel):
    title:str
    content:str
    published: bool=True

class PostCreate(PostBase):
    pass


class VpnBase(BaseModel):
    nombreClienteExterno:str
    direccionIPRoshka:str
    direccionIPCliente:str
    marcaEquipoRoshka:str
    versionEquipoRoshka:str
    marcaEquipoCliente:str
    versionEquipoCliente:str
    claveCompartida:str
    esquemaDeEncriptacion:str
    grupoDH:str
    algoritmoEncriptacion_fase1:str
    hash_fase1:str
    lifetime_fase1:int
    algoritmoEncriptacion_fase2:str
    hash_fase2:str
    pfs:bool=False
    lifetime_fase2:int
    dominioEncriptacionRoshka:str
    dominoEncriptacionCliente:str
	
class VpnCreate(VpnBase):
    pass

class VpnUpdateRoshka(VpnBase):
    pass

class VpnUpdateCliente(BaseModel):
    nombreClienteExterno:str
    direccionIPCliente:str
    marcaEquipoCliente:str
    versionEquipoCliente:str
    dominoEncriptacionCliente:str





