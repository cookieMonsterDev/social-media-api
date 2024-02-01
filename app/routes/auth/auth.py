from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
import bcrypt

from ...database import get_session
from .models import CreateUserDto, LoginUserDto
from ..users.models import User

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(loginUserDto: LoginUserDto, db: Session = Depends(get_session)):

    return {"test": loginUserDto}


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(createUserDto: CreateUserDto, db: Session = Depends(get_session)):

    # is_email_taken = db.get(User, {"email": createUserDto.email})
    # if is_email_taken:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT, detail="email is taken")

    hash = hash_password(createUserDto.password)

    new_user = User(username=createUserDto.username,
                    email=createUserDto.email, hash=hash)

    print(new_user)

    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    return new_user
