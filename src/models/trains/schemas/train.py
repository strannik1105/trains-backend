from pydantic import BaseModel
from pydantic.datetime_parse import date

from models.stations.schemas.station import Station


# from models.wagons.schemas.wagon import Wagon


class TrainBase(BaseModel):
    sid: int
    name: str
    description: str
    operation_data: date


class Train(TrainBase):
    train_st_disl: Station
    train_st_dest: Station


class TrainCreate(TrainBase):
    train_st_disl_sid: int
    train_st_dest_sid: int
