from common.repository.repository import AbstractRepository
from models.users import User

user_repository = AbstractRepository[User](User)
