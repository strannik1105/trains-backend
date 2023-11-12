from sqlalchemy import String, Column, ForeignKey, Integer, Date
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel
from models.stations import Station

TRAIN_SCHEMA = "trains"


class Train(BaseModel):
    __table_args__ = {"schema": TRAIN_SCHEMA, "comment": "Table with all trains"}
    sid = Column(Integer, primary_key=True)

    name = mapped_column(String)
    description = mapped_column(String)
    operation_data = mapped_column(Date)
    train_st_disl_sid = mapped_column(ForeignKey(Station.sid))
    train_st_dest_sid = mapped_column(ForeignKey(Station.sid))

    train_st_disl = relationship(
        Station, foreign_keys=[train_st_disl_sid], lazy="joined"
    )
    train_st_dest = relationship(
        Station, foreign_keys=[train_st_dest_sid], lazy="joined"
    )
