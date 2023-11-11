import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from common.enums.enums import Role
from models.stations.schemas.station import Station
from models.trains.schemas.train import TrainBase, Train


class WagonBase(BaseModel):
    sid: int
    wagon_st_disl: Station
    wagon_st_dest: Station
    train: Train


class Wagon(WagonBase):
    ...


class WagonCreate(WagonBase):
    ...
