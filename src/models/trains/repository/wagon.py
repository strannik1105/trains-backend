from clickhouse_driver import Client

from common.repository.repository import AbstractRepository
from models.trains.wagon import Wagon


class WagonRepository(AbstractRepository[Wagon]):
    def get_historical_data(self, db: Client):
        objs = db.execute("SELECT train_id, operdate, desl_id, dest_id, train_id FROM wagons_telemetry ")
        return objs

    def get_historical_data_by_train(self, db: Client, train_id: str):
        objs = db.execute(
            f"SELECT wagon_id, operdate, desl_id, dest_id, train_id FROM wagons_telemetry WHERE train_id = '{train_id}'")
        return objs

    def get_historical_data_by_wagon(self, db, wagon_id):
        objs = db.execute(
            f"SELECT wagon_id, operdate, desl_id, dest_id, train_id FROM wagons_telemetry WHERE wagon_id = '{wagon_id}'")
        return objs

    def get_wagons_by_station(self, db, station_id):
        objs = db.execute(
            f"SELECT DISTINCT wagon_id, operdate, train_id FROM wagons_telemetry WHERE desl_id = '{station_id}' ORDER BY operdate DESC")
        return objs

    def get_wagons_by_station_and_train(self, db, station_id, train_sid):
        objs = db.execute(
            f"SELECT DISTINCT wagon_id, operdate, train_id FROM wagons_telemetry WHERE desl_id = '{station_id}' AND train_id = '{train_sid}' ORDER BY operdate DESC")
        return objs


wagon_repository = WagonRepository(Wagon)
