from typing import Optional

from pydantic import BaseModel

from models.stations.schemas.station import Station


# from models.trains.schemas.train import TrainBase, Train


class WagonBase(BaseModel):
    sid: int
    name: Optional[str]
    description: Optional[str]


class Wagon(WagonBase):
    wagon_st_disl: Station
    wagon_st_dest: Station


class WagonCreate(WagonBase):
    wagon_st_disl_sid: int
    wagon_st_dest_sid: int
    train_sid: int


class WagonUpdate(BaseModel):
    wagon_st_disl_sid: int
    wagon_st_dest_sid: int
    train_sid: int
