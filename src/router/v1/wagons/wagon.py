from typing import List
from uuid import UUID

from fastapi import APIRouter, Path

from models.wagons import Wagon, wagon_repository
from models.wagons.schemas import wagon
from router.deps import PGSession

router = APIRouter()


@router.get("/", response_model=List[wagon.Wagon])
async def get_wagons(db: PGSession):
    db_objs = await wagon_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=wagon.Wagon)
async def get_wagon(db: PGSession, sid: UUID = Path(description="сид вагона")):
    db_obj = await wagon_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=wagon.Wagon)
async def create_user(db: PGSession, new_wagon: wagon.WagonCreate):
    obj = Wagon(**new_wagon.__dict__)
    db_obj = await wagon_repository.create(db, obj, with_commit=True)
    return db_obj


