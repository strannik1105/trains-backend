from typing import List
from uuid import UUID

from fastapi import APIRouter, Path

from models.trains import Train, train_repository
from models.trains.schemas import train
from router.deps import PGSession

router = APIRouter()


@router.get("/", response_model=List[train.Train])
async def get_trains(db: PGSession):
    db_objs = await train_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=train.Train)
async def get_train(db: PGSession, sid: UUID = Path(description="сид поезда")):
    db_obj = await train_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=train.Train)
async def create_train(db: PGSession, new_train: train.TrainCreate):
    obj = Train(**new_train.__dict__)
    db_obj = await train_repository.create(db, obj, with_commit=True)
    return db_obj




