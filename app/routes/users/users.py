from fastapi import APIRouter, Depends, status
from sqlmodel import Session

# from ..database import get_session

router = APIRouter(
  prefix='/users',
  tags=['users']
)

# @router.get('/')
# async def get_users(db: Session = Depends(get_session)):
#   return { "allusers": [] }


# @router.get('/{id}')
# async def get_user_by_id(id: int, db: Session = Depends(get_session)):
#     return { "userId": id }


# @router.put('/{id}')
# async def get_user_by_id(id: int, db: Session = Depends(get_session)):
#     return { "userId": id }


# @router.delete('/{id}')
# async def get_user_by_id(id: int, db: Session = Depends(get_session)):
#     return { "userId": id }