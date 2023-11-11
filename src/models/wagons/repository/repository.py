from common.repository.repository import AbstractRepository
from models.wagons import Wagon

wagon_repository = AbstractRepository[Wagon](Wagon)
