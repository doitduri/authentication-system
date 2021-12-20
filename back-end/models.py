from sqlalchemy import Column, String, Boolean, Integer

from databases.config import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True)
    password = Column(String(200))
    is_admin = Column(Boolean)
