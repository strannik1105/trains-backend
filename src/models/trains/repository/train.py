from common.repository.repository import AbstractRepository
from models.trains.train import Train

train_repository = AbstractRepository[Train](Train)
