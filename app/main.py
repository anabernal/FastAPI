
from fastapi import FastAPI, Response,status,HTTPException, Depends,Form, Request, APIRouter
from fastapi.params import Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session 

import time
from .import models, schemas 

from .database import engine, get_db
from .routers import post, vpn
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(vpn.router)
app.include_router(post.router)


