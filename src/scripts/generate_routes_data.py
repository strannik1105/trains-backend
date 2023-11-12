import csv

import psycopg2
from faker import Faker
from psycopg2.errors import ForeignKeyViolation
import settings

faker = Faker()


def convert_id_to_int(value: str) -> int:
    value = value.replace(',', '')
    return int(value)


def convert_to_float(value: str) -> float:
    value = value.replace(',', '.')
    return float(value)


def generate_routes():
    conn = psycopg2.connect(
        f"host={settings.POSTGRES_HOST} port={settings.POSTGRES_PORT} "
        f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}")
    conn.autocommit = True
    cur = conn.cursor()
    routes_meta = open("routes_meta.csv", newline='')
    reader = csv.DictReader(routes_meta)
    for row in reader:
        query = (f"INSERT INTO stations.route (node1_sid, node2_sid, length) "
                 f"VALUES ({convert_id_to_int(row['START_CODE'])}, {convert_id_to_int(row['END_CODE'])}, {convert_id_to_int(row['LEN'])});")
        try:
            cur.execute(query)
        except ForeignKeyViolation as e:
            print(e)


if __name__ == "__main__":
    generate_routes()
