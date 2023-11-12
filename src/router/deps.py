from typing import Annotated

from clickhouse_driver import Client
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session, get_ch_connection

PGSession = Annotated[AsyncSession, Depends(get_pg_session)]
CHSession = Annotated[Client, Depends(get_ch_connection)]
