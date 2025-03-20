# Gestor de VPNs  
Esta aplicacion permite crear registros de configuraciones de VPNs para las entidades que deseen levantar VPNs IPSec con la empresa Roshka.
Cuenta con todas las tareas de CRUD ademas de una visualizacion de JSON por cada registro creado.


## Tecnologías utilizadas:  
**Backend**:   
*  FastAPI.  
*  SQLModel para las interacciones  con la base de datos.  
*  Pydantict, para las validaciones.  
*  Postgres como servidor SQL  
**Frontend**:  
*  Jinja2 para las plantillas web  
*  Bootsrap

## Como utilizar:    
**1. Crear un repositorio y clonar el repositorio de manera manual, ejemplo**:  
```git clone https://github.com/anabernal/FastAPI.git```

## Requerimientos:   
**1. Crear y activar un virtual environmet https://fastapi.tiangolo.com/virtual-environments/ e instalar FastAPI:**  
``` pip install "fastapi[standard]"```  
**2. Verificar que se haya instalado correctamente:**  
``` fastapi dev main.py  ```  
**2. Instalar uvicorn:**  
```pip install "uvicorn[standard]"  ```  
**3. Instalar sqlalchemy:**  
```pip install python-multipart sqlalchemy jinja2```  
**5. Instalar jinja2:**  
```pip install python-multipart sqlalchemy jinja2```  

## Configuración:
**1. En el archivo database.py, modificar las credenciales de base de datos en la línea:**  
```SQLALCHEMY_URL_DATABASE='postgresql://postgres:postgres@localhost:5432/fastapi'  ```  
Campos: basededatos://usuario:contraseña**
**2. De ser necesario, crear el main.py en el directorio /app:**  
```
from fastapi.templating import Jinja2Templates
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session 
import time
from .import models, schemas 
from .database import engine, get_db
from .routers import  vpn
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(vpn.router)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/vpns")

```
**3. Correr FastAPI:**  
```python -m uvicorn app.main:app --reload```  
**4. Navegar hasta el link:**   
http://127.0.0.1:8000/vpns  
**5. Pagina principal:**  
Se visualizan los atributos basicos de la VPN, como ID, Nombre del cliente externo, rol de la VPN(Primario o Secundario) y las acciones que se puedan realizar con el registro, como editar, editar los parametros del cliente, eliminar y visualizar a traves del formato  json.  
![image](https://github.com/user-attachments/assets/fd8dc21e-29e7-411e-bb9b-3810a86585ac)  
## 4. Documentos de API iteractivos:
Navegar hasta el link  
http://127.0.0.1:8000/docs  
![image](https://github.com/user-attachments/assets/7de89b38-71a3-4fd5-99f4-7451fdf9f864)  
Para ver la documentación automática alternativa (proporcionada por ReDoc), navegar hasta el link:  
http://127.0.0.1:8000/redoc  
![image](https://github.com/user-attachments/assets/2518454e-287c-4a35-b38e-15a29383cd07)  



## 5. Futuras mejoras:  
*  Autenticación de usuarios para ingresar a la aplicacion con sus correspondientes permisos para editar discriminando por tipos de usuarios (externos e internos)  
*  Validaciones para ingresar correctamente las IPs publicas e IPs privadas  
*  Botón de script para generar configuraciones dependiendo de la marca del dispositivo  


