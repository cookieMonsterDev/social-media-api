from sqlmodel import Session, SQLModel, create_engine
from .config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, echo=True)


def create_tables_and_engine():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
