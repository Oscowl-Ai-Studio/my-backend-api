from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# We define the variables directly here to avoid system environment conflicts
DB_USER = "utkarshasalokhe"
DB_PASS = "Ups292001"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "utkarshasalokhe_db"

DATABASE_URL = f"postgresql://utkarshasalokhe:Ups292001@db:5432/utkarshasalokhe_db"

print(f"DEBUG: Attempting to connect to: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()