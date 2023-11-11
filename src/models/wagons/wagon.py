from sqlalchemy import String, Column, UUID, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel
from models.stations import Station
from models.trains import Train

WAGON_SCHEMA = "wagons"


class Wagon(BaseModel):
    __table_args__ = {"schema": WAGON_SCHEMA, "comment": "Table with all wagons"}
    sid = Column(Integer, primary_key=True)

    name = mapped_column(String)
    description = mapped_column(String)
    wagon_st_disl_sid = mapped_column(ForeignKey(Station.sid))
    wagon_st_dest_sid = mapped_column(ForeignKey(Station.sid))
    train_sid = mapped_column(ForeignKey(Train.sid))

    wagon_st_disl = relationship(Station, foreign_keys=[wagon_st_disl_sid], lazy='joined')
    wagon_st_dest = relationship(Station, foreign_keys=[wagon_st_dest_sid], lazy='joined')
    train = relationship(Train, foreign_keys=[train_sid], lazy='joined')

