from common.repository.repository import AbstractRepository
from models.trains import Train

train_repository = AbstractRepository[Train](Train)
