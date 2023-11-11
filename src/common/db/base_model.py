import uuid

from sqlalchemy import Column, UUID
from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlalchemy.orm import declared_attr

decl_base = declarative_base()


@as_declarative()
class BaseModel:

    # Generate table name automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
