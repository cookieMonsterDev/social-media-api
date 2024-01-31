from fastapi import APIRouter

router = APIRouter(
  prefix='/posts',
  tags=['posts']
)

@router.get('/')
async def get_users():
  return { "allposts": [] }

@router.get('/{id}')
async def get_user_by_id(id: int):
    return { "postId": id }