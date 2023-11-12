from fastapi import APIRouter, Path

from common.exceptions.error_codes import ErrorCodes
from common.exceptions.exceptions import BackendException
from models.trains.repository.wagon import wagon_repository
from models.trains.repository.train import train_repository
from models.trains.wagon import Wagon
from models.trains.schemas import wagon
from router.deps import PGSession, CHSession

router = APIRouter()


@router.get("/", response_model=list[wagon.Wagon])
async def get_wagons(db: PGSession):
    db_objs = await wagon_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=wagon.Wagon)
async def get_wagon(db: PGSession, sid: int = Path(description="сид вагона")):
    db_obj = await wagon_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=wagon.Wagon)
async def create_wagon(db: PGSession, new_wagon: wagon.WagonCreate):
    train = await train_repository.get(db, sid=new_wagon.train_sid)
    if train is None:
        raise BackendException(ErrorCodes.not_allow)
    obj = Wagon(**new_wagon.__dict__)
    db_obj = await wagon_repository.create(db, obj, with_commit=True)
    return db_obj


@router.put("/{sid}", response_model=wagon.Wagon)
async def update(
        db: PGSession,
        updated_obj: wagon.WagonUpdate,
        sid: int = Path(description="сид"),
):
    db_obj = await wagon_repository.get(db, sid)
    updated_obj = {k: v for k, v in updated_obj.__dict__.items() if v is not None}
    db_obj = await wagon_repository.update(db, db_obj, updated_obj)
    return db_obj


@router.get("/{sid}/historical/by_train")
async def get_historical_data_by_train(db: CHSession, sid: str = Path(description="сид поезда")):
    db_objs = wagon_repository.get_historical_data_by_train(db, train_id=sid)
    response = [
        {"wagon_id": i[0], "operdate": i[1], "st_desl_id": i[2], "st_dest_id": i[3], "train_id": i[4]} for i in db_objs
    ]
    return response


@router.get("/{sid}/historical/by_wagon")
async def get_historical_data_by_wagon(db: CHSession, sid: str = Path(description="сид вагона")):
    db_objs = wagon_repository.get_historical_data_by_wagon(db, wagon_id=sid)
    response = [
        {"wagon_id": i[0], "operdate": i[1], "st_desl_id": i[2], "st_dest_id": i[3], "train_id": i[4]} for i in db_objs
    ]
    return response
