from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_URL_DATABASE='postgresql://postgres:postgres@localhost:5432/fastapi'
engine=create_engine(SQLALCHEMY_URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

#dependencies
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
