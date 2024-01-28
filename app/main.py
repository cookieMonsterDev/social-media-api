from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import psycopg

app = FastAPI()

try:
   conn = psycopg.connect(f"""
    dbname=mydb
    user=johndoe
    password=randompassword
    host=localhost
    port=5432""")
except:
    print("sadjask")

class CreatePostDto(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
     {
        "id": 1,
        "title": "test 12",
        "content": "test content",
        "published": True,
        "rating": None
    },
    {
        "id": 2,
        "title": "test 12",
        "content": "test content",
        "published": True,
        "rating": None
    },
    {
        "id": 3,
        "title": "test 12",
        "content": "test content",
        "published": True,
        "rating": None
    }
]

def findPostById(id: int):
    for item in my_posts:
        if item['id'] == id:
            return item
    return None    
    
@app.get("/posts")
def get_posts():
    return my_posts

@app.get('/posts/{id}')
def get_post(id: int):
    data = findPostById(id) 
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=None)
    return { "data": data }

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    my_posts.append(data)
    return jsonable_encoder(data)

@app.patch('/posts/{id}')
def update_post(id: int, createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    my_posts[id] = data
    return jsonable_encoder(data)

@app.delete('/posts/{id}')
def delete_post(id: int):
    del my_posts[id]
    return