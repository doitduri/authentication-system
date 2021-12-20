from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SECRET_KEY = "duri.auth.assignment"
ALGORITHM = "HS256"

DATABASE_ACCOUNT = 'root'
DATABASE_PASSWORD = ''

DATABASE_URL = "mysql+mysqldb://DATABASE_ACCOUNT:DATABASE_PASSWOR@fastapi-auth.cjvmghmvhslq.eu-west-1.rds.amazonaws.com:3306/auth"
engine = create_engine(
    DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
