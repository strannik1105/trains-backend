from uuid import UUID

from common.schemas.base import PydanticBase
from models.stations.schemas.station import Station


class RouteBase(PydanticBase):
    node1: Station
    node2: Station
    length: int


class Route(RouteBase):
    sid: int
