from sqlmodel import SQLModel, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

from ..config import get_settings

settings = get_settings()

DATABASE_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autoflush=False, expire_on_commit=False, bind=engine)

# Base = declarative_base()