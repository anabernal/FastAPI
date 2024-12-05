from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publised: bool =True

my_posts=[{"title": "title of post 1", "content":"content of post 1", "id":1},{"title": "title of post 2", "content":"content of post 2", "id":2}]
def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
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
    post_dict=post.dict()
    post_dict['id']=randrange(0,10000)
    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/posts/{id}")
def get_posts(id:int):
    post=find_post(id)
    return {"post_detail": post}
    
