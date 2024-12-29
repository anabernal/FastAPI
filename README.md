Tecnologías utilizadas:  
Backend:    
    -FastAPI  
    -SQLModel para las interacciones  con la base de datos  
    -Pydantict, para las validaciones  
    -Postgres como servidor SQL  
Frontend:  
    -Jinja2 para las plantillas web
    -Bootsrap


Como utilizar:
Crear un repositorio
Clonar el repositorio de manera manual, ejemplo:
git clone https://github.com/anabernal/FastAPI.git
Requerimientos:
Crear y activar un virtual environmet https://fastapi.tiangolo.com/virtual-environments/ e instalar FastAPI:
$ pip install "fastapi[standard]"
Verificar que se haya instalado correctamente:
$ fastapi dev main.py
Instalar uvicorn:
pip install "uvicorn[standard]"
Instalar sqlalchemy
Instalar jinja2:




Configuracion:
En el archive database.py, modificar las credenciales de base de datos en la línea:
SQLALCHEMY_URL_DATABASE='postgresql://postgres:postgres@localhost:5432/fastapi'
Campos: basededatos://usuario:contraseña



