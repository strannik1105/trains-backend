from typing import Optional

from common.schemas.base import PydanticBase


class StationBase(PydanticBase):
    name: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]


class Station(StationBase):
    sid: int


class StationCreate(StationBase):
    pass


class StationUpdate(StationBase):
    pass


class StationFilter(StationBase):
    sid: Optional[int]
