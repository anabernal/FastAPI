from .. import models,schemas
from fastapi import FastAPI, Response,status,HTTPException, Depends,Form, APIRouter, Request
from sqlalchemy.orm import Session 
from .. database import engine, get_db
from fastapi.templating import Jinja2Templates
import json
router=APIRouter(
    prefix="/posts",
    tags=['Post']
)
import os

templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

@router.get("/")
def test_post(request:Request, db:Session=Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts""")
    #posts=cursor.fetchall()
    posts=db.query(models.Post).all()
    return{"data": posts}
    #return templates.TemplateResponse("index.html", {"request": request,"posts":posts })

@router.get("/list")
def get_posts():
    posts = db.query*(models.Post).all()
    return json([posts.to_json() for p in posts])



    return json.dumps([posts.to_json() for p in posts])



@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post:schemas.PostCreate, db:Session=Depends(get_db)):
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



@router.get("/{id}")
def get_post(id:int, db: Session=Depends(get_db)):
  #cursor.execute(""" SELECT * FROM POSTS WHERE ID=%s""", (str(id)))
  #post=cursor.fetchone()
  #print(post)
  post=db.query(models.Post).filter(models.Post.id==id).first()
  if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"post with {id} was not found")
  return {"post_detail":post}



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session=Depends(get_db)): 
    #cursor.execute(
    #    """DELETE FROM posts WHERE id=%s returning *""",(str(id)))
    #deleted_post=cursor.fetchone()
    #conn.commit()
    post=db.query(models.Post).filter(models.Post.id==id)
    if post.first()==None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail =f"post with {id} does not exists")
    #este comando elimina el post:
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}")
def update_post(id:int, updated_post:schemas.PostCreate, db:Session=Depends(get_db)):
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

