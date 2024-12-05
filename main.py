from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publised: bool =True

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/")
def get_user():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post:Post):
    print(post)
    print(post.dict())
    return{"data": "new post"}
    
@app.get("/posts/{id}")
def get_post(id:int):
  post=find_post(id)
  print(id)
  return {"post_detail":post}