

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.config import settings

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

def check_db():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
    except OperationalError as e:
        raise RuntimeError("Database is not ready") from e


