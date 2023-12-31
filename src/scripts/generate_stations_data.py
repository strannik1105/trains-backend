import csv
import time

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


def generate_stations():
    conn = psycopg2.connect(
        f"host={settings.POSTGRES_HOST} port={settings.POSTGRES_PORT} "
        f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}")
    conn.autocommit = True
    cur = conn.cursor()
    st_meta = open("stations_meta.csv", newline='')
    reader = csv.DictReader(st_meta)
    st_meta = {row['ST_ID']: {"lat": row["LATITUDE"], "long": row["LONGITUDE"]} for row in reader}
    for k, v in st_meta.items():
        if (v['lat'] is None) or (v['lat'] == ''):
            lat = 'null'
        else:
            lat = convert_to_float(v['lat'])
        if (v['long'] is None) or (v['long'] == ''):
            long = 'null'
        else:
            long = convert_to_float(v['long'])
        query = (f"INSERT INTO stations.station (sid, name, latitude, longitude) "
                 f"VALUES ({convert_id_to_int(k)}, '{faker.name()}', {lat}, {long}) "
                 f"ON CONFLICT (sid) DO NOTHING;")
        cur.execute(query)
    conn.commit()


def create_root_user():
    conn = psycopg2.connect(
        f"host={settings.POSTGRES_HOST} port={settings.POSTGRES_PORT} "
        f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD}")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users.user (sid, name, email, password, role) VALUES (gen_random_uuid(), 'root', 'root@root.com', 'pass', 'SUPERUSER')"
    )


if __name__ == "__main__":
    generate_stations()
