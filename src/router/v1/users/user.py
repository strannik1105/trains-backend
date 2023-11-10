from typing import List
from uuid import UUID

from fastapi import APIRouter, Path

from models.users import User, user_repository
from models.users.schemas import user
from router.deps import PGSession

router = APIRouter()


@router.get("/", response_model=List[user.User])
async def get_users(db: PGSession):
    db_objs = await user_repository.get_all(db)
    return db_objs


@router.get("/{sid}", response_model=user.User)
async def get_user(db: PGSession, sid: UUID = Path(description="сид пользователя")):
    db_obj = await user_repository.get(db, sid)
    return db_obj


@router.post("/", response_model=user.User)
async def create_user(db: PGSession, new_user: user.UserCreate):
    obj = User(**new_user.__dict__)
    db_obj = await user_repository.create(db, obj, with_commit=True)
    return db_obj


@router.put("/{sid}", response_model=user.User)
async def update_user(
        db: PGSession,
        updated_user: user.UserUpdate,
        sid: UUID = Path(description="сид пользователя"),
):
    db_obj = await user_repository.get(db, sid)
    db_obj = await user_repository.update(db, db_obj, updated_user.__dict__)
    return db_obj


@router.delete("/{sid}")
async def delete_user(db: PGSession, sid: UUID = Path(description="сид пользователя")):
    db_obj = await user_repository.get(db, sid)
    await user_repository.remove(db, db_obj)
    return {"msg": "success"}
