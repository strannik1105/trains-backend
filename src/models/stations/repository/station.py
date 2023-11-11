from common.repository.repository import AbstractRepository
from models.stations import Station

station_repository = AbstractRepository[Station](Station)
