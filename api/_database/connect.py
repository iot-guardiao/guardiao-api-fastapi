import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DB_URI")

engine = create_engine(
    DATABASE_URL,
    pool_size=10,            
    max_overflow=40,
    pool_timeout=360,
    pool_recycle=3600,
    pool_pre_ping=True # Valida a conexão antes de usá-la
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
