from typing import List

from fastapi import APIRouter, Path

from common.schemas.messages import Msg
from models.trains.repository.train import train_repository
from models.trains.repository.wagon import wagon_repository
from models.users import User
from models.stations.repository.station import station_repository
from models.stations.schemas import station
from router.deps import PGSession, CHSession

router = APIRouter()


@router.get("/", response_model=List[station.Station])
async def get_all(db: PGSession):
    db_objs = await station_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=station.Station)
async def get_one(db: PGSession, sid: int = Path(description="сид")):
    db_obj = await station_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=station.StationBase)
async def create(db: PGSession, new_user: station.StationCreate):
    obj = User(**new_user.__dict__)
    db_obj = await station_repository.create(db, obj, with_commit=True)
    return db_obj


@router.put("/{sid}", response_model=station.Station)
async def update(
        db: PGSession,
        updated_obj: station.StationUpdate,
        sid: int = Path(description="сид"),
):
    db_obj = await station_repository.get(db, sid)
    updated_obj = {k: v for k, v in updated_obj.__dict__.items() if v is not None}
    db_obj = await station_repository.update(db, db_obj, updated_obj)
    return db_obj


@router.delete("/{sid}", response_model=Msg)
async def delete(db: PGSession, sid: int = Path(description="сид")):
    db_obj = await station_repository.get(db, sid)
    await station_repository.remove(db, db_obj)
    return {"msg": "success"}


@router.get("/{sid}/wagons")
async def get_wagons(db: CHSession, sid: int = Path(description="сид")):
    db_objs = wagon_repository.get_wagons_by_station(db, station_id=sid)
    response = [
        {"wagon_id": i[0], "operdate": i[1], "train_id": i[2]} for i in db_objs
    ]
    return response


@router.get("/{sid}/wagons/{train_sid}")
async def get_wagons_on_train(db: CHSession, sid: int = Path(description="сид"),
                              train_sid: str = Path(description="сид поезда")):
    db_objs = wagon_repository.get_wagons_by_station_and_train(db, station_id=sid, train_sid=train_sid)
    response = [
        {"wagon_id": i[0], "operdate": i[1], "train_id": i[2]} for i in db_objs
    ]
    return response


@router.get("/{sid}/trains")
async def get_trains(db: CHSession, sid: int = Path(description="сид")):
    db_objs = train_repository.get_wagons_by_station(db, station_id=sid)
    response = [
        {"train_id": i[0], "operdate": i[1]} for i in db_objs
    ]
    return response
