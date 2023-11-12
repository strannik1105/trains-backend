import csv

from common.db.session import get_ch_connection


def remove_spaces(value: str) -> int:
    return int(value.replace(' ', ''))


def generate_test_data():
    meta = open("hist_data_meta.csv", newline='')
    reader = csv.DictReader(meta)
    ch = get_ch_connection()
    for row in reader:
        wagon_id = row['WAGNUM']
        if wagon_id is None:
            continue
        operdate = row['OPERDATE']
        if operdate is None:
            continue
        st_id_disl = row['ST_ID_DISL']
        if st_id_disl is None:
            continue
        st_id_dest = row['ST_ID_DEST']
        if st_id_dest is None:
            continue
        train_index = row['TRAIN_INDEX']
        if train_index is None:
            continue
        query = ("INSERT INTO wagons_telemetry (wagon_id, operdate, desl_id, dest_id, train_id) VALUES("
                 f"{remove_spaces(wagon_id)}, "
                 f"'{operdate}', "
                 f"{remove_spaces(st_id_disl)}, "
                 f"{remove_spaces(st_id_dest)}, "
                 f"'{train_index}'"
                 ")")
        try:
            ch.execute(query)
        except Exception as e:
            print("Error on")
            print(query)


if __name__ == "__main__":
    generate_test_data()
