from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from common.enums.enums import Role
from models.stations.schemas.station import Station
from models.wagons.schemas.wagon import Wagon


class TrainBase(BaseModel):
    sid: int
    train_st_disl: Station
    train_st_dest: Station
    operation_data: str


class Train(TrainBase):
    wagon: list[Wagon]


class TrainCreate(TrainBase):
    ...
