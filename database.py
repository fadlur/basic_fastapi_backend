from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup untuk sqlite
# DATABASE_URL = "sqlite:///./uploads.db"

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Setup untuk postgresql
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="147789"
POSTGRES_DB="fastapi_dev"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"

DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()