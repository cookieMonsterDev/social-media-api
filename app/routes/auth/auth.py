from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select

from ...database import get_session
from .models import CreateUserDto, LoginUserDto
from ..users.models import User

from ...utils.hash import hash_password, verify_password

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(loginUserDto: LoginUserDto, db: Session = Depends(get_session)):

    is_user_exist = db.exec(select(User).where(
        User.email == loginUserDto.email)).first()

    if not is_user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There is no user with such an email.")

    is_password_match = verify_password(
        loginUserDto.password, is_user_exist.hash)

    if not is_password_match:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong credentials")

    return is_user_exist


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(createUserDto: CreateUserDto, db: Session = Depends(get_session)):

    is_email_taken = db.exec(select(User).where(
        User.email == createUserDto.email)).first()

    if is_email_taken:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email is taken")

    hash = hash_password(createUserDto.password)

    new_user = User(username=createUserDto.username,
                    email=createUserDto.email, hash=hash)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
