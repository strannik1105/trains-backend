from typing import Optional
from uuid import UUID

from common.enums.enums import Role
from common.schemas.base import PydanticBase


class UserBase(PydanticBase):
    name: Optional[str]
    email: Optional[str]
    role: Optional[Role]


class User(UserBase):
    sid: UUID


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    old_password: Optional[str]
    new_password: Optional[str]
