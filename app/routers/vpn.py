from .. import models,schemas
from fastapi import Response,status,HTTPException, Depends,Form, APIRouter,Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session 
from ..database import engine, get_db
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import os

templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

router=APIRouter(
    tags=['Vpn']
)

@router.get("/vpns")
def get_vpns(request:Request, db:Session=Depends(get_db)):
    vpns=db.query(models.Vpn).all()
    #return{"data": vpns}
    return templates.TemplateResponse("index.html", {"request": request,"vpns":vpns })



@router.post("/vpns", status_code=status.HTTP_201_CREATED)
def create_vpns(vpn:schemas.VpnCreate, db:Session=Depends(get_db)):
    new_vpn=models.Vpn(
        **vpn.model_dump())
    db.add(new_vpn)
    db.commit()
    db.refresh(new_vpn)
    return{"data":new_vpn}

@router.get("/vpns/{id}")
def get_vpn(id:int, db: Session=Depends(get_db)):
  vpn=db.query(models.Vpn).filter(models.Vpn.id==id).first()
  if not vpn:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Vpn con ID {id} no existente")
  return {"vpn_detail":vpn}


"""@router.put("update/{id}")
def update_vpn(id:int, update_vpn:schemas.VpnUpdateCliente, db:Session=Depends(get_db)):
    vpn_query=db.query(models.Vpn).filter(models.Vpn.id==id)
    vpn=vpn_query.first()
    if vpn==None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"VPN con ID  {id} no existente")
    vpn_query.update(update_vpn.model_dump(), synchronize_session=False)
    db.commit()
    return{'data':vpn_query.first()}"""

@router.get("/vpns/edit/{id}")
def edit(request: Request, id: int, db: Session = Depends(get_db)):
    vpn = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "vpn": vpn})

@router.post("/vpns/update/{id}")
def update(request: Request, id: int,nombreClienteExterno: str = Form(...),db: Session = Depends(get_db)):
    vpns = db.query(models.Vpn).filter(models.Vpn.id == id).first()
    vpns.nombreClienteExterno = nombreClienteExterno
    db.commit()
    #return RedirectResponse(url=router.url_path_for("index.html"), status_code=status.HTTP_303_SEE_OTHER)
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



     