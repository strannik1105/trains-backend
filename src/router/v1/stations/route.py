from typing import List

from fastapi import APIRouter, Path

from common.services.graph_service import GraphService
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


@router.get("/shortest/{sid1}/{sid2}", response_model=List[route.Route])
async def get_shortest_path(
    db: PGSession,
    sid1: int = Path(description="сид1"),
    sid2: int = Path(description="сид2"),
):
    db_objs = await route_repository.get_all(db)

    GraphService().create_graph(db_objs)

    return GraphService().shortest_path(sid1, sid2)


@router.get("/length/{sid1}/{sid2}")
async def get_length_of_path(
    db: PGSession,
    sid1: int = Path(description="сид1"),
    sid2: int = Path(description="сид2"),
):
    db_objs = await route_repository.get_all(db)

    GraphService().create_graph(db_objs)

    return GraphService().length_of_path(sid1, sid2)
