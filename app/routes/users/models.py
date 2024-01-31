from typing import List
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from ..posts.models import Post

class User(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    posts: List[Post] = Relationship(back_populates="user")
    created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=False)