from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

class User(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    posts: List[Post] = Relationship(back_populates="user")
    created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=False)

class Post(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    published: bool = Field(default=True, nullable=False)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="posts")
    created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=False)
