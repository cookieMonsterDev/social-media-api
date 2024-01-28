from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel, ValidationError

app = FastAPI()

class CreatePostDto(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/posts')
def create_post(createPostDto: CreatePostDto):
    try: 
        return { "test": createPostDto.title }
    except ValidationError as error:
        return { "error": 'test error' }