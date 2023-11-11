from typing import List

from fastapi import APIRouter, Path

from models.stations.repository.route import route_repository
from models.stations.schemas import route
from router.deps import PGSession

router = APIRouter()


@router.get("/", response_model=List[route.Route])
async def get_all(db: PGSession):
    db_objs = await route_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=route.Route)
async def get_one(db: PGSession, sid: int = Path(description="сид")):
    db_obj = await route_repository.get(db, sid)
    return db_obj
