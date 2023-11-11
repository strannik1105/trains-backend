import uuid
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from common.enums.enums import Role
from models.trains.schemas.train import TrainBase


class WagonBase(BaseModel):
    wagon_indx: int
    wagon_st_disl: uuid
    wagon_st_dest: uuid


class Wagon(WagonBase):
    sid: UUID


class WagonCreate(WagonBase):
    ...
