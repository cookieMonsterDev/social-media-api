from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

# from ..posts.models import Post

class User(SQLModel, table=True):
    id: Optional[int] = Field(nullable=False, primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    hash: str = Field(nullable=False)
    # posts: List[Post] = Relationship(back_populates="user")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)