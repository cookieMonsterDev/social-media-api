from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.auth import auth
from .routes.posts import posts
from .routes.users import users
from .database import create_tables_and_engine

app = FastAPI()

create_tables_and_engine()

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
