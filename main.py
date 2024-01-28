from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class CreatePostDto(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = []

@app.get("/posts")
def get_posts():
    return my_posts

@app.get('/posts/{id}')
def get_post(id: int):
    data = my_posts[id]
    return jsonable_encoder(data)

@app.post('/posts')
def create_post(createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    my_posts.append(data)
    return jsonable_encoder(data)

@app.patch('/posts/{id}')
def update_post(id: int, createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    my_posts[id] = data
    return jsonable_encoder(data)

@app.delete('posts/{id}')
def delete_post(id: int):
    del my_posts[id]
    return