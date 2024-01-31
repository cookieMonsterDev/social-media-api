from sqlmodel import Session, SQLModel, create_engine
from .config import get_settings

settings = get_settings()

DATABASE_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True , connect_args=connect_args)


def create_tables_and_engine():
  SQLModel.metadata.create_all(engine)

def get_session():
  with Session(engine) as session:
    yield session