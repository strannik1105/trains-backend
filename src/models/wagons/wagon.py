from sqlalchemy import String, Column, UUID, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel

WAGON_SCHEMA = "wagons"


class Wagon(BaseModel):
    __table_args__ = {"schema": WAGON_SCHEMA, "comment": "Table with all wagons"}

    name = Column(String, nullable=True)  # Не обязательное название
    description = Column(String, nullable=True)  # Не обязательное описание
    wagon_indx = Column(Integer, nullable=False)  # вагона поезда
    wagon_st_disl = Column(UUID, ForeignKey('station.sid'))  # станция отправки вагона
    wagon_st_dest = Column(UUID, ForeignKey('station.sid'))  # конечная станция вагона
    train_indx = Column(Integer, ForeignKey('train.train_indx'))  # номер поезда текущего вагона

    train = relationship('Train', back_populates='wagon')
    station = relationship('Station', back_populates='wagon')