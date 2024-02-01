from sqlmodel import SQLModel
from typing_extensions import Annotated
from pydantic import EmailStr, StringConstraints


class LoginUserDto(SQLModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(
        strip_whitespace=True, to_upper=True, min_length=8, max_length=16)]


class CreateUserDto(LoginUserDto):
    username: str
