from common.repository.repository import AbstractRepository
from models.stations import Route


class RouteRepository(AbstractRepository[Route]):
    pass


route_repository = RouteRepository(Route)
