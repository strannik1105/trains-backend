from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.repository.repository import AbstractRepository
from models.users import User
from router.v1.authentication.ext import verify_password


class UserRepository(AbstractRepository[User]):
    async def get_by_email(self, session: AsyncSession, email: str) -> Optional[User]:  # noqa
        query = await session.execute(
            select(User).filter(User.email == email)
        )
        return query.scalar()

    async def authenticate(self, session: AsyncSession, *, email: str, password: str) -> Optional[User]:
        user_obj = await self.get_by_email(session, email=email)
        if not user_obj:
            return None
        if not verify_password(password, user_obj):
            return None
        return user_obj


user_repository = UserRepository(User)
