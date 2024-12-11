from pydantic import BaseModel
class PostBase(BaseModel):
    title:str
    content:str
    published: bool=True

class PostCreate(PostBase):
    pass


class VpnBase(BaseModel):
    direccionIPRoshka:str
    direccionIPCliente:str
    clienteExterno:str
    marcaEquipoRoshka:str
    versionEquipoRoshka:str
    marcaEquipoCliente:str
    versionEquipoCliente:str
    claveCompartida:str
    esquemaDeEncriptacion:str
    grupoDH:str
    mainOAggressive:str
    lifetime:int
    encapsulacion:bool=True
    algoritmoEncriptacion:str
    pfs=bool
    lifetime:str
    dominioEncriptacionRoshka:str
    dominoEncriptacionCliente:str

class VpnCreate(PostBase):
    pass

class VpnUpdateRoshka(PostBase):
    pass

class VpnUpdateCliente(PostBase):
    clienteExterno:str
    direccionIPCliente:str
    marcaEquipoCliente:str
    versionEquipoCliente:str
    claveCompartida:str
    dominoEncriptacionCliente:str


