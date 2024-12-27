import argparse
import pandas as pd
from datetime import datetime 
import sqlite3

def main(csv_path: str) -> None:
    rows_df = pd.read_csv(csv_path)
    rows_dict_list = rows_df.to_dict("records")
    base_query = "INSERT INTO people (name,last_name,age) VALUES"
    values_list = [tuple(row.values()) for row in rows_dict_list]
    ## SQLITE
    try:
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        cursor.executemany(f'{base_query}(?,?,?)', values_list)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Mass CSV data import',
                    description='Imports csv data to a db table already created'
            )
    parser.add_argument('-f', '--file', type=str)      # CSV File Path to import
    args = parser.parse_args()
    file_path = args.file
    logger = logging.getLogger(__name__)
    start = datetime.now()
    main(file_path)
    print(f'Time elapsed: {datetime.now() - start}')
