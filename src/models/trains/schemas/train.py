from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from common.enums.enums import Role
from models.wagons.schemas.wagon import Wagon


class TrainBase(BaseModel):
    train_indx: int
    train_st_disl: Station
    train_st_dest: Station
    operation_data: Optional[str]


class Train(TrainBase):
    sid: UUID
    wagon: list[Wagon]


class TrainCreate(TrainBase):
    ...
