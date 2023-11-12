from common.repository.repository import AbstractRepository
from models.trains.wagon import Wagon

wagon_repository = AbstractRepository[Wagon](Wagon)
