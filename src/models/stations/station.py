from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import mapped_column

from common.db.base_model import BaseModel

SCHEMA = "stations"


class Station(BaseModel):
    __table_args__ = {"schema": SCHEMA, "comment": "Table with all stations"}
    sid = mapped_column(Integer, primary_key=True)  # because in tables it's int.....
    name = mapped_column(String)
    longitude = mapped_column(Float)
    latitude = mapped_column(Float)
