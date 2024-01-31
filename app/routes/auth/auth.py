from fastapi import APIRouter, Depends, status
from sqlmodel import Session
# from ..database.models import Post

from ...database import get_session
# from app.routes.users.models import User

router = APIRouter(
  prefix='/auth',
  tags=['auth']
)

@router.post('/login', status_code=status.HTTP_200_OK)
async def get_users(loginUserDto, db: Session = Depends(get_session)):
  return { "allauth": [] }


# @router.post('/register', status_code=status.HTTP_201_CREATED)
# async def get_user_by_id(registerUserDto, db: Session = Depends(get_session)):
#     return { "authId": id }