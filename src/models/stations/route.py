import uuid

from sqlalchemy import ForeignKey, Integer, UUID
from sqlalchemy.orm import mapped_column, relationship

from common.db.base_model import BaseModel
from models.stations.station import Station

SCHEMA = "stations"


class Route(BaseModel):
    __table_args__ = {"schema": SCHEMA, "comment": "Table with all stations"}
    sid = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=lambda: uuid.uuid4().hex,
    )
    node1_sid = mapped_column(ForeignKey(Station.sid))
    node2_sid = mapped_column(ForeignKey(Station.sid))
    length = mapped_column(Integer)

    node1 = relationship(Station, foreign_keys=[node1_sid])
    node2 = relationship(Station, foreign_keys=[node2_sid])
