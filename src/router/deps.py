from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session

PGSession = Annotated[AsyncSession, Depends(get_pg_session)]
