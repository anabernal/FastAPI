
from fastapi import FastAPI, Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .import models 
from sqlalchemy.orm import Session 
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


    
class Post(BaseModel):
    title:str
    content:str
    published: bool=True

while True:
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',
                                user='postgres', password='postgres', 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
    except Exception as error:
        print("Connecting to Database failed")
        print("Error", error)
        time.sleep(2)

my_posts=[{"title":"title of post 1", "content": "content of post 1","id": 1}, {"title":"favorite foods", "content":"sushi, asado", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p["id"]==id:
            return id


@app.get("/sqlalchemy")
def test_post(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return{"data": posts}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post, db:Session=Depends(get_db)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING *""" ,
    #               (post.title, post.content, post.publised))
    #new_post=cursor.fetchone()
    #conn.commit()
   # print(**post.model_dump())
    new_post=models.Post(
        **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":new_post}
    
@app.get("/posts/{id}")
def get_post(id:int, db: Session=Depends(get_db)):
  #cursor.execute(""" SELECT * FROM POSTS WHERE ID=%s""", (str(id)))
  #post=cursor.fetchone()
  #print(post)
  post=db.query(models.Post).filter(models.Post.id==id).first()
  if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} was not found")
  return {"post_detail":post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session=Depends(get_db)): 
    #cursor.execute(
    #    """DELETE FROM posts WHERE id=%s returning *""",(str(id)))
    #deleted_post=cursor.fetchone()
    #conn.commit()
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first==None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail =f"post with {id} does not exists")
    #este comando elimina el post:
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, updated_post:Post, db:Session=Depends(get_db)):
    #cursor.execute("""UPDATE posts SET title= %s, content=%s, published=%s 
    #               WHERE id=%s RETURNING * """,(post.title,post.content,post.publised,str(id)))
    #update_post=cursor.fetchone()
    #conn.commit()
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} does not exists")
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return{'data':post_query.first()}
