from .. import models,schemas
from fastapi import Response,status,HTTPException, Depends,Form, APIRouter,Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session 
from ..database import engine, get_db
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from ipaddress import IPv4Address, IPv4Network
import os

templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

router=APIRouter(
    tags=['Vpn']
)
router.mount("/routers/vpns",StaticFiles(directory="app/routers/"))


@router.get("/vpns")
def get_vpns(request:Request, db:Session=Depends(get_db)):
    vpns=db.query(models.Vpn).all()
    #return{"data": vpns}
    return templates.TemplateResponse("index.html", {"request": request,"vpns":vpns })


@router.post("/vpns/add")
async def add(
    request: Request, 
    nombreClienteExterno:str= Form(...),
    rol:str= Form(...),
    direccionIPRoshka:str= Form(...),
    direccionIPCliente:str= Form(...),
    marcaEquipoRoshka:str= Form(...),
    versionEquipoRoshka:str= Form(...),
    marcaEquipoCliente:str= Form(...),
    versionEquipoCliente:str= Form(...),
    claveCompartida:str= Form(...),
    esquemaDeEncriptacion:str= Form(...),
    grupoDH:str= Form(...),
    algoritmoEncriptacion_fase1:str= Form(...),
    hash_fase1:str= Form(...),
    lifetime_fase1:int= Form(...),
    algoritmoEncriptacion_fase2:str= Form(...),
    hash_fase2:str= Form(...),
    pfs:str= Form(...),
    lifetime_fase2:int= Form(...),
    dominioEncriptacionRoshka:str= Form(...),
    dominoEncriptacionCliente:str= Form(...), 
    db: Session = Depends(get_db)):

    

    vpn = models.Vpn(
    nombreClienteExterno =nombreClienteExterno,
    rol =rol,
    direccionIPRoshka=direccionIPRoshka,
    direccionIPCliente=direccionIPCliente,
    marcaEquipoRoshka=marcaEquipoRoshka,
    versionEquipoRoshka=versionEquipoRoshka,
    marcaEquipoCliente=marcaEquipoCliente,
    versionEquipoCliente=versionEquipoCliente,
    claveCompartida=claveCompartida,
    esquemaDeEncriptacion=esquemaDeEncriptacion,
    grupoDH=grupoDH,
    algoritmoEncriptacion_fase1=algoritmoEncriptacion_fase1,
    hash_fase1=hash_fase1,
    lifetime_fase1=lifetime_fase1,
    algoritmoEncriptacion_fase2=algoritmoEncriptacion_fase2,
    hash_fase2=hash_fase2,
    pfs=pfs,
    lifetime_fase2=lifetime_fase2,
    dominioEncriptacionRoshka=dominioEncriptacionRoshka,
    dominoEncriptacionCliente=dominoEncriptacionCliente)
    db.add(vpn)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_vpns"), status_code=status.HTTP_303_SEE_OTHER)

@router.post("/vpns", status_code=status.HTTP_201_CREATED)
def create_vpns(vpn:schemas.VpnCreate, db:Session=Depends(get_db)):
    new_vpn=models.Vpn(
        **vpn.model_dump())
    db.add(new_vpn)
    db.commit()
    db.refresh(new_vpn)
    return{"data":new_vpn}

@router.get("/vpns/addnew")
def addnew(request: Request):
    return templates.TemplateResponse("addnew.html", {"request": request})

@router.get("/vpns/{id}")
def get_vpn(id:int, db: Session=Depends(get_db)):
  vpn=db.query(models.Vpn).filter(models.Vpn.id==id).first()
  if not vpn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Vpn con ID {id} no existente")
  return {"vpn_detail":vpn}


@router.get("/vpns/edit/{id}")
def edit(request: Request, id: int, db: Session = Depends(get_db)):
    vpn = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "vpn": vpn})

@router.get("/vpns/editcliente/{id}")
def edit(request: Request, id: int, db: Session = Depends(get_db)):
    vpn = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    return templates.TemplateResponse("editcliente.html", {"request": request, "vpn": vpn})

@router.post("/vpns/update/{id}")
def update(request: Request,         
    id: int, 
    nombreClienteExterno: str = Form(...),
    rol: str = Form(...),
    direccionIPRoshka: str = Form(...),
    direccionIPCliente: str = Form(...),
    marcaEquipoRoshka:str= Form(...),
    versionEquipoRoshka:str= Form(...),
    marcaEquipoCliente:str= Form(...),
    versionEquipoCliente:str= Form(...),
    claveCompartida:str= Form(...),
    esquemaDeEncriptacion:str= Form(...),
    grupoDH:str= Form(...),
    algoritmoEncriptacion_fase1:str= Form(...),
    hash_fase1:str= Form(...),
    lifetime_fase1:int= Form(...),
    algoritmoEncriptacion_fase2:str= Form(...),
    hash_fase2:str= Form(...),
    pfs:str= Form(...),
    lifetime_fase2:int= Form(...),
    dominioEncriptacionRoshka:str= Form(...),
    dominoEncriptacionCliente:str= Form(...), 
    db: Session = Depends(get_db)):

    vpns = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    vpns.nombreClienteExterno = nombreClienteExterno
    vpns.rol=rol
    vpns.direccionIPRoshka = direccionIPRoshka
    vpns.direccionIPCliente=direccionIPCliente
    nombreClienteExterno =nombreClienteExterno,
    rol =rol,
    direccionIPRoshka=direccionIPRoshka,
    direccionIPCliente=direccionIPCliente,
    marcaEquipoRoshka=marcaEquipoRoshka,
    versionEquipoRoshka=versionEquipoRoshka,
    marcaEquipoCliente=marcaEquipoCliente,
    versionEquipoCliente=versionEquipoCliente,
    claveCompartida=claveCompartida,
    esquemaDeEncriptacion=esquemaDeEncriptacion,
    grupoDH=grupoDH,
    algoritmoEncriptacion_fase1=algoritmoEncriptacion_fase1,
    hash_fase1=hash_fase1,
    lifetime_fase1=lifetime_fase1,
    algoritmoEncriptacion_fase2=algoritmoEncriptacion_fase2,
    hash_fase2=hash_fase2,
    pfs=pfs,
    lifetime_fase2=lifetime_fase2,
    dominioEncriptacionRoshka=dominioEncriptacionRoshka,
    dominoEncriptacionCliente=dominoEncriptacionCliente
    

    db.commit()
    return RedirectResponse(url=router.url_path_for("get_vpns"), status_code=status.HTTP_303_SEE_OTHER)

@router.get("/vpns/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_vpnt(request: Request, id: int, db: Session = Depends(get_db)):
    vpn = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    if vpn==None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail =f"Vpn con ID {id} no existente")
    #este comando elimina el post:
    db.delete(vpn)
    db.commit()
    return RedirectResponse(url=router.url_path_for("get_vpns"), status_code=status.HTTP_303_SEE_OTHER)



     