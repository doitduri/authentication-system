from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "email": "john@gmail.com",
                "password": "password"
            }
        }


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "john",
                "password": "password"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '15f1480539fe42fb4bd10ff3a84793dd10aaac55a627004969d5cda75c5c1f2a'


@AuthJWT.load_config
def get_config():
    return Settings()
