from fastapi import APIRouter, Path

from common.exceptions.error_codes import ErrorCodes
from common.exceptions.exceptions import BackendException
from models.trains.repository.train import train_repository
from models.trains.schemas import train
from models.trains.train import Train
from router.deps import PGSession

router = APIRouter()


@router.get("/")
async def get_trains(db: PGSession):
    db_objs = await train_repository.get_all(db)
    return db_objs


@router.get("/{sid}")
async def get_train(db: PGSession, sid: int = Path(description="сид поезда")):
    db_obj = await train_repository.get(db, sid)
    return db_obj


@router.post("/")
async def create_train(db: PGSession, new_train: train.TrainCreate):
    obj = Train(**new_train.__dict__)
    db_obj = await train_repository.create(db, obj, with_commit=True)
    if db_obj is None:
        raise BackendException(ErrorCodes.incorrect_credentials)
    return db_obj
