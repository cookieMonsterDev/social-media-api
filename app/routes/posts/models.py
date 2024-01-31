from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

from ..users.models import User

class Post(SQLModel, table=True):
    id: int = Field(nullable=False, primary_key=True)
    title: str = Field(nullable=False)
    content: str = Field(nullable=False)
    published: bool = Field(default=True, nullable=False)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="posts")
    created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=False)