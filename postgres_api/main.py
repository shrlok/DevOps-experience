import psycopg2
from datetime import datetime

dt = datetime.now()
class PostgresApi():
    def __init__(self):
        self.connection = psycopg2.connect(
            host = "127.0.0.1",
            user = "postgres",
            password = "password",
            database = "test_db"
        )
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True


    def create_table(self):
        try:
            create_table = ''' CREATE TABLE test_table
                (Id serial PRIMARY KEY,
                Text text NOT NULL,
                Date timestamp
                )
                '''
            self.cursor.execute(create_table)
            print("table created")
        except Exception as _ex:
            print("[INFO] Error whith PostgrSQL: ", _ex)

    def put_data(self, data):

        try:
            add_data = f''' INSERT INTO test_table (Text, Date) VALUES('{data}', '{dt}'); '''
            self.cursor.execute(add_data)

        except Exception as _ex:
            print("[INFO] Error whith PostgrSQL: ", _ex)


con = PostgresApi()
con.create_table()
con.put_data("hello")