from common.repository.repository import AbstractRepository
from models.trains.train import Train


class TrainRepository(AbstractRepository[Train]):
    def get_wagons_by_station(self, db, station_id):
        objs = db.execute(
            f"SELECT DISTINCT train_id, operdate FROM wagons_telemetry WHERE desl_id = '{station_id}' ORDER BY operdate DESC")
        return objs

    def get_all_available_trains(self, db):
        objs = db.execute(
            f"SELECT DISTINCT train_id FROM wagons_telemetry")
        return objs


train_repository = TrainRepository(Train)
