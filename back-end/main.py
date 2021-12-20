from datetime import timedelta
from http.client import HTTPException
from typing import List

import bcrypt
import jwt
from fastapi import FastAPI, security
from fastapi.params import Depends, Header, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBasicCredentials, OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT

from sqlalchemy.orm import Session

import models
from databases.config import Base, SessionLocal, engine, get_db, SECRET_KEY, ALGORITHM
from schema import User, UserLogin

Base.metadata.create_all(engine)
app = FastAPI()


@app.get('/')
def index():
    return {"message": "hello"}


@app.get('/users', response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()


@app.post('/users/signup')
def create_user(user: UserLogin, db: Session = Depends(get_db)):
    is_joined = get_user_by_email(db, user_email=user.email)
    if is_joined:
        raise HTTPException(status_code=400, detail="Email already registered")

    password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = models.User(email=user.email, password=password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.post('/users/login')
def login(user: UserLogin, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    logined_user = get_user_by_email(db, user_email=user.email)

    if logined_user:
        access_token = jwt.encode(
            {"user_email": user.email},
            SECRET_KEY,
            algorithm=ALGORITHM,
        )

        refresh_token = jwt.encode(
            {"user_email": user.email},
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return {"access_token": access_token, "refresh_token": refresh_token}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")


oauth_schema = OAuth2PasswordBearer(tokenUrl='/token')


@app.get('/users/me')
def get_user_info(token: HTTPAuthorizationCredentials = Security(oauth_schema), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("user_email")
        user = get_user_by_email(db, user_email=user_email)
        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
