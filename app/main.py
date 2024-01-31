from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.auth import auth
from .routes.posts import posts
from .routes.users import users

# from typing import Optional
# from fastapi import status, HTTPException
# from pydantic import BaseModel
 
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

@app.get('/')
def root():
    return { "message": "This api is working" }

# @app.get("/posts")
# def get_posts():
#     return

# @app.get('/posts/{id}')
# def get_post(id: int):
#     data = None
#     if not data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=None)
#     return { "data": data }

# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# def create_post(createPostDto: CreatePostDto):
#     data = createPostDto.model_dump()
#     return jsonable_encoder(data)

# @app.patch('/posts/{id}')
# def update_post(id: int, createPostDto: CreatePostDto):
#     data = createPostDto.model_dump()
#     return jsonable_encoder(data)

# @app.delete('/posts/{id}')
# def delete_post(id: int):
#     return