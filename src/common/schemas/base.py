from datetime import datetime

import orjson
import pytz
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


def datetime_with_tz(dt: datetime) -> str:
    # if not dt.tzinfo:
    dt = dt.replace(tzinfo=pytz.timezone("Europe/Moscow"))

    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


class PydanticBase(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        json_encoders = {datetime: datetime_with_tz}
        orm_mode = True
