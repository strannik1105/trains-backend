from fastapi import APIRouter, Path

from common.exceptions.error_codes import ErrorCodes
from common.exceptions.exceptions import BackendException
from models.wagons.repository.repository import wagon_repository

from models.wagons.schemas import wagon
from models.wagons.wagon import Wagon
from router.deps import PGSession

router = APIRouter()


@router.get("/")
async def get_wagons(db: PGSession):
    db_objs = await wagon_repository.get_all(db)
    return db_objs


@router.get("/{sid}")
async def get_wagon(db: PGSession, sid: int = Path(description="сид вагона")):
    db_obj = await wagon_repository.get(db, sid)
    print(type(db_obj))
    return db_obj


@router.post("/")
async def create_wagon(db: PGSession, new_wagon: wagon.WagonCreate):
    obj = Wagon(**new_wagon.__dict__)
    db_obj = await wagon_repository.create(db, obj, with_commit=True)
    if db_obj is None:
        raise BackendException(ErrorCodes.incorrect_credentials)
    return db_obj


@router.put("/{sid}")
async def update(
    db: PGSession,
    updated_obj: wagon.WagonUpdate,
    sid: int = Path(description="сид"),
):
    db_obj = await wagon_repository.get(db, sid)
    updated_obj = {k: v for k, v in updated_obj.__dict__.items() if v is not None}
    db_obj = await wagon_repository.update(db, db_obj, updated_obj)
    return db_obj
