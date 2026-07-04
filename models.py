from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String, unique=True)

    name = Column(String)

    address = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Application(Base):

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    reference = Column(String, unique=True)

    phone = Column(String)

    service = Column(String)

    sub_service = Column(String)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )