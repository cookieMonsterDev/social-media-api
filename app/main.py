from typing import Optional
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from app.database.database import Base, engine
 

app = FastAPI()

class CreatePostDto(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
 
    
@app.get("/posts")
def get_posts():
    return

@app.get('/posts/{id}')
def get_post(id: int):
    data = None
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=None)
    return { "data": data }

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    return jsonable_encoder(data)

@app.patch('/posts/{id}')
def update_post(id: int, createPostDto: CreatePostDto):
    data = createPostDto.model_dump()
    return jsonable_encoder(data)

@app.delete('/posts/{id}')
def delete_post(id: int):
    return