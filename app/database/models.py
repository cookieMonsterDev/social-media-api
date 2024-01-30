from typing import Optional, List
from sqlalchemy import TIMESTAMP
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

# class Post(SQLModel, table=True):
#     id: int = Field(nullable=False, primary_key=True)
#     title: str = Field(nullable=False)
#     content: str = Field(nullable=False)
#     published: bool = Field(default=True, nullable=False)
#     user_id: int = Field(foreign_key="user.id")
#     user: User = Relationship(back_populates="posts")
#     created_at: datetime = Field(default=datetime.utcnow)
#     updated_at: datetime = Field(default=datetime.utcnow)


# class User(SQLModel, table=True):
#     id: int = Field(nullable=False, primary_key=True)
#     email: str = Field(nullable=False, unique=True)
#     password: str = Field(nullable=False)
#     created_at: TIMESTAMP = Field()

# class Vote(SQLModel, table=True):
#     id: int = Field(nullable=False, primary_key=True)
#     user_id: int = Field(Integer, ForeignKey(
#         "users.id", ondelete="CASCADE"), primary_key=True)
#     post_id: int = Field(ForeignKey(
#         "posts.id", ondelete="CASCADE"), primary_key=True)