import settings
from common.db.session import get_ch_connection


def create_wagons_table():
    ch = get_ch_connection()
    ch.execute("CREATE TABLE IF NOT EXISTS wagons_telemetry ("
               "wagon_id Integer, "
               "operdate DateTime, "
               "desl_id Integer, "
               "dest_id Integer, "
               "train_id String"
               ")"
               "Engine = MergeTree() "  # if we won't to store duplicates use ReplacingMergeTree(but on test we want)
               "ORDER BY (wagon_id, operdate)"
               )


def connect_to_rabbit():
    ch = get_ch_connection()
    ch.execute("CREATE TABLE IF NOT EXISTS wagons_broker_handler ("
               "wagon_id Integer, "
               "operdate DateTime, "
               "desl_id Integer, "
               "dest_id Integer, "
               "train_id String"
               ")"
               "Engine = RabbitMQ SETTINGS "
               f"rabbitmq_host_port = '{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}', "
               f"rabbitmq_username = '{settings.RABBITMQ_USER}', "
               f"rabbitmq_password = '{settings.RABBITMQ_PASSWORD}', "
               f"rabbitmq_exchange_name = '{settings.RABBITMQ_PARSER_EXCHANGE}', "
               f"rabbitmq_skip_broken_messages = 10, "
               f"rabbitmq_exchange_type = 'topic', "
               f"rabbitmq_routing_key_list = '#', "
               f"rabbitmq_format = 'JSONEachRow'"
               )
    ch.execute("CREATE MATERIALIZED VIEW IF NOT EXISTS wagons_broker_bridge TO wagons_telemetry AS SELECT "
               "wagon_id, "
               "operdate, "
               "desl_id, "
               "dest_id, "
               "train_id "
               "FROM wagons_broker_handler")


if __name__ == "__main__":
    create_wagons_table()
