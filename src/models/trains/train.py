from sqlalchemy import String, Column, ForeignKey, UUID, Integer, Date
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel

TRAIN_SCHEMA = "trains"


class Train(BaseModel):
    __table_args__ = {"schema": TRAIN_SCHEMA, "comment": "Table with all trains"}

    name = Column(String, nullable=True)  # не обязательное название
    description = Column(String, nullable=True)  # не обязательное описание
    operation_data = Column(Date)  # дата отправки поезда
    train_indx = Column(Integer, nullable=False)  # номер поезда
    train_st_disl = Column(UUID, ForeignKey('station.sid'))  # начальная станция поезда
    train_st_dest = Column(UUID, ForeignKey('station.sid'))  # конечная станция поезда

    wagon = relationship('Wagon', back_populates='train')
    station = relationship('Station', back_populates='train')